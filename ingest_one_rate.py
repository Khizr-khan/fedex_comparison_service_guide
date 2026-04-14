"""
ingest_one_rate.py — Adds FedEx One Rate data to existing ChromaDBs.

Extracted from:
  - FedEx 2026 Service Guide PDF page 46
  - FedEx 2025 Service Guide PDF page 46

Run AFTER ingest_excel.py and ingest_excel_2025.py:
    python ingest_one_rate.py

This script APPENDS to existing DBs — does NOT delete them.
"""

import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

CHROMA_DIR_2026 = "./chroma_fedex_db"
CHROMA_DIR_2025 = "./chroma_fedex_db_2025"
EMBED_MODEL     = "all-MiniLM-L6-v2"

SERVICE = "FedEx One Rate®"

# ── Zone definitions ──────────────────────────────────────────────────────────
ZONES = {
    "Local Zone 2":        "Zone 2",
    "Regional Zones 3-4":  "Zones 3-4",
    "National Zones 5-8":  "Zones 5-8",
}

# ── Package types ─────────────────────────────────────────────────────────────
PACKAGE_TYPES = [
    "FedEx Envelope",
    "FedEx Pak",
    "FedEx Small Box",
    "FedEx Medium Box",
    "FedEx Large Box",
    "FedEx Extra Large Box",
    "FedEx Tube",
]

# ── Services ──────────────────────────────────────────────────────────────────
SERVICES = [
    "FedEx Express Saver®",
    "FedEx 2Day®",
    "FedEx 2Day® A.M.",
    "FedEx Standard Overnight®",
    "FedEx Priority Overnight®",
    "FedEx First Overnight®",
]

# ── 2026 Rates [zone][package][service] ──────────────────────────────────────
# Order: ES, 2Day, 2DayAM, SO, PO, FO
RATES_2026 = {
    "Local Zone 2": {
        "FedEx Envelope":        [11.90, 11.90, 33.80, 37.30,  46.25, 100.25],
        "FedEx Pak":             [15.25, 15.25, 39.25, 47.60,  56.40, 110.40],
        "FedEx Small Box":       [18.25, 18.25, 40.95, 51.15,  57.45, 111.45],
        "FedEx Medium Box":      [22.75, 22.75, 41.80, 55.50,  66.30, 120.30],
        "FedEx Large Box":       [29.95, 29.95, 43.50, 66.95,  73.85, 127.85],
        "FedEx Extra Large Box": [39.95, 39.95, 54.50, 76.00,  87.80, 141.80],
        "FedEx Tube":            [39.95, 39.95, 54.50, 76.00,  87.80, 141.80],
    },
    "Regional Zones 3-4": {
        "FedEx Envelope":        [11.90, 11.90, 36.90,  38.85,  61.75, 115.75],
        "FedEx Pak":             [15.25, 15.25, 40.95,  66.00,  92.55, 146.55],
        "FedEx Small Box":       [18.25, 18.25, 41.80,  72.00, 100.80, 154.80],
        "FedEx Medium Box":      [22.75, 22.75, 45.70,  76.00, 114.85, 168.85],
        "FedEx Large Box":       [29.95, 29.95, 54.50,  91.50, 130.40, 184.40],
        "FedEx Extra Large Box": [39.95, 39.95, 69.70, 123.95, 170.65, 224.65],
        "FedEx Tube":            [39.95, 39.95, 69.70, 123.95, 170.65, 224.65],
    },
    "National Zones 5-8": {
        "FedEx Envelope":        [11.90, 11.90,  50.40,  51.95,  76.60, 130.60],
        "FedEx Pak":             [15.25, 15.25,  59.55,  85.35, 123.75, 177.75],
        "FedEx Small Box":       [18.25, 18.25,  68.80,  95.10, 138.50, 192.50],
        "FedEx Medium Box":      [22.75, 22.75,  86.90,  98.90, 156.70, 210.70],
        "FedEx Large Box":       [29.95, 29.95, 108.90, 137.10, 180.40, 234.40],
        "FedEx Extra Large Box": [39.95, 39.95, 157.55, 190.50, 250.50, 304.50],
        "FedEx Tube":            [39.95, 39.95, 157.55, 190.50, 250.50, 304.50],
    },
}

# ── 2025 Rates [zone][package][service] ──────────────────────────────────────
RATES_2025 = {
    "Local Zone 2": {
        "FedEx Envelope":        [10.95, 10.95, 31.90, 35.20,  43.65,  97.65],
        "FedEx Pak":             [13.75, 13.75, 37.05, 44.95,  53.25, 107.25],
        "FedEx Small Box":       [16.75, 16.75, 38.65, 48.30,  54.25, 108.25],
        "FedEx Medium Box":      [21.00, 21.00, 39.45, 52.40,  62.60, 116.60],
        "FedEx Large Box":       [28.50, 28.50, 41.10, 63.20,  69.75, 123.75],
        "FedEx Extra Large Box": [37.75, 37.75, 51.45, 71.75,  82.90, 136.90],
        "FedEx Tube":            [37.75, 37.75, 51.45, 71.75,  82.90, 136.90],
    },
    "Regional Zones 3-4": {
        "FedEx Envelope":        [10.95, 10.95, 34.85,  37.35,  58.30, 112.30],
        "FedEx Pak":             [13.75, 13.75, 38.65,  63.45,  87.40, 141.40],
        "FedEx Small Box":       [16.75, 16.75, 39.45,  69.25,  95.20, 149.20],
        "FedEx Medium Box":      [21.00, 21.00, 43.15,  73.10, 108.45, 162.45],
        "FedEx Large Box":       [28.50, 28.50, 51.45,  88.00, 123.15, 177.15],
        "FedEx Extra Large Box": [37.75, 37.75, 65.80, 119.20, 161.15, 215.15],
        "FedEx Tube":            [37.75, 37.75, 65.80, 119.20, 161.15, 215.15],
    },
    "National Zones 5-8": {
        "FedEx Envelope":        [10.95, 10.95,  47.60,  49.95,  72.35, 126.35],
        "FedEx Pak":             [13.75, 13.75,  56.25,  82.05, 116.85, 170.85],
        "FedEx Small Box":       [16.75, 16.75,  64.95,  91.45, 130.80, 184.80],
        "FedEx Medium Box":      [21.00, 21.00,  82.05,  95.10, 147.95, 201.95],
        "FedEx Large Box":       [28.50, 28.50, 102.85, 131.85, 170.35, 224.35],
        "FedEx Extra Large Box": [37.75, 37.75, 148.75, 183.15, 236.55, 290.55],
        "FedEx Tube":            [37.75, 37.75, 148.75, 183.15, 236.55, 290.55],
    },
}


def build_docs(rates, year, source):
    """Build Document objects for all One Rate combinations."""
    docs = []
    for zone_label, packages in rates.items():
        for pkg_type, svc_rates in packages.items():
            for svc_idx, service in enumerate(SERVICES):
                rate = svc_rates[svc_idx]
                # Short service name for text
                svc_short = (service
                    .replace("FedEx ", "")
                    .replace("®", "")
                    .strip())

                text = (
                    f"FedEx One Rate. Zone: {zone_label}. "
                    f"Package type: {pkg_type}. "
                    f"Service: {service}. "
                    f"Flat rate: ${rate:.2f}."
                )
                meta = {
                    "source": source,
                    "page": 46,
                    "type": "one_rate",
                    "year": year,
                    "service": SERVICE,
                    "underlying_service": service,
                    "zone": zone_label,
                    "package_type": pkg_type,
                    "weight": "any",  # One Rate is weight-independent (up to limit)
                }
                docs.append(Document(page_content=text, metadata=meta))
    return docs


def ingest_to_db(docs, chroma_dir, year):
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
    vs = Chroma(persist_directory=chroma_dir, embedding_function=embeddings)

    before = vs._collection.count()
    BATCH = 500
    for i in range(0, len(docs), BATCH):
        batch = docs[i:i + BATCH]
        vs.add_documents(batch)
        print(f"  Inserted batch {i // BATCH + 1} ({len(batch)} chunks)")

    after = vs._collection.count()
    print(f"  {chroma_dir}: {before} → {after} chunks (+{after - before})")


def main():
    print("\n" + "=" * 55)
    print("FedEx One Rate Ingestion")
    print("=" * 55)

    # ── 2026 ──────────────────────────────────────────────────────────────────
    print(f"\nBuilding 2026 One Rate docs...")
    docs_2026 = build_docs(RATES_2026, "2026", "FedEx_Service_Guide_2026")
    print(f"  {len(docs_2026)} One Rate chunks built")
    print(f"Appending to {CHROMA_DIR_2026}...")
    ingest_to_db(docs_2026, CHROMA_DIR_2026, "2026")

    # ── 2025 ──────────────────────────────────────────────────────────────────
    print(f"\nBuilding 2025 One Rate docs...")
    docs_2025 = build_docs(RATES_2025, "2025", "FedEx_Service_Guide_2025")
    print(f"  {len(docs_2025)} One Rate chunks built")
    print(f"Appending to {CHROMA_DIR_2025}...")
    ingest_to_db(docs_2025, CHROMA_DIR_2025, "2025")

    print("\n" + "=" * 55)
    print(f"✅ Done. {len(docs_2026) + len(docs_2025)} total One Rate chunks added.")
    print("=" * 55)
    print("\nNext steps:")
    print("  1. Re-upload both DBs to HuggingFace")
    print("  2. Restart HuggingFace Space")


if __name__ == "__main__":
    main()