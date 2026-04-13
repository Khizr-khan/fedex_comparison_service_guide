"""
get_2025_rates.py — Fetches the actual 2025 rates from ChromaDB for comparison test cases.
Run: python get_2025_rates.py
This tells you the exact expected_2025 values to put in evaluate.py
"""
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vs = Chroma(persist_directory="./chroma_fedex_db_2025", embedding_function=embeddings)

queries = [
    ("Priority Overnight zone 4, 10 lbs",   "FedEx Priority Overnight®",                "Zone 4",         "10"),
    ("First Overnight zone 7, 3 lbs",        "FedEx First Overnight®",                   "Zone 7",         "3"),
    ("Ground zone 3, 20 lbs",               "FedEx Ground® and FedEx Home Delivery®",   "Zone 3",         "20"),
    ("Express Saver zone 8, 5 lbs",          "FedEx Express Saver®",                     "Zone 8",         "5"),
    ("2Day zone 6, 40 lbs",                  "FedEx 2Day®",                              "Zone 6",         "40"),
    ("Intl Priority zone D, 81 lbs",         "FedEx International Priority®",            "Zone D",         "81"),
    ("Connect Plus zone F, 97 lbs",          "FedEx® International Connect Plus",        "Zone F",         "97"),
    ("Wrong address fee",                    None,                                        None,             None),
    ("Adult signature required fee",         None,                                        None,             None),
    ("Yukon surcharge",                      None,                                        None,             None),
]

print("=" * 65)
print("2025 RATES FROM CHROMADB")
print("=" * 65)

for label, service, zone, weight in queries:
    print(f"\n  {label}")
    if service is None:
        # Surcharge — use similarity search
        results = vs.similarity_search(label, k=1, filter={"type": {"$eq": "surcharge"}})
        if results:
            print(f"    → {results[0].page_content}")
        continue

    r = vs._collection.get(
        where={"$and": [
            {"service": {"$eq": service}},
            {"zone":    {"$eq": zone}},
            {"weight":  {"$eq": weight}},
        ]},
        include=["documents"]
    )
    if r["documents"]:
        for doc in r["documents"]:
            print(f"    → {doc}")
    else:
        print(f"    ❌ Not found (service={service}, zone={zone}, weight={weight})")