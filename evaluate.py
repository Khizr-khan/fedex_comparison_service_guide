"""
Evaluate the RAG engine against all 20 verified test cases.
Run after ingestion is complete:
    python evaluate_fedex.py

Requires uvicorn to be running locally on port 8000:
    uvicorn main:app --host 0.0.0.0 --port 8000
"""

import json
import requests

BACKEND = "http://localhost:8000"

TEST_CASES = [
    {"question": "Priority Overnight zone 4, 10 lbs",                     "expected": "$151.83"},
    {"question": "First Overnight zone 7, 3 lbs",                         "expected": "$168.19"},
    {"question": "Standard Overnight zone 5, 30 lbs",                     "expected": "$314.80"},
    {"question": "2Day zone 6, 40 lbs",                                   "expected": "$344.55"},
    {"question": "2Day AM zone 7, 75 lbs",                                "expected": "$735.71"},
    {"question": "Express Saver zone 8, 5 lbs",                           "expected": "$69.71"},
    {"question": "Ground zone 3, 20 lbs",                                 "expected": "$21.77"},
    {"question": "Intl Economy Puerto Rico, 101 lbs",                     "expected": "$791.84"},
    {"question": "Intl Priority zone D, 81 lbs",                          "expected": "$1,558.22"},
    {"question": "Intl First Canada zone A, 59 lbs",                      "expected": "$745.89"},
    {"question": "Intl Priority Express zone J, 91 lbs",                  "expected": "$2,825.66"},
    {"question": "Connect Plus zone F, 97 lbs",                           "expected": "$1,291.01"},
    {"question": "Wrong address fee",                                      "expected": "$25.50"},
    {"question": "Saturday delivery fee Priority Overnight",              "expected": "$16"},
    {"question": "Oversize charge zone 5 home delivery",                  "expected": "$320"},
    {"question": "Automated weekly pickup cost",                          "expected": "$19"},
    {"question": "Yukon 50lb international ground surcharge",             "expected": "$110"},
    {"question": "Adult signature required fee",                          "expected": "$10"},
    {"question": "Senseaware domestic journey cost",                      "expected": "$150"},
    {"question": "Redirect package within 120 miles fee",                 "expected": "$5.55"},
]


def ask(question: str) -> str:
    resp = requests.post(
        f"{BACKEND}/ask-stream",
        json={"question": question, "top_k": 5, "history": []},
        stream=True,
        timeout=30,
    )
    return "".join(chunk.decode() for chunk in resp.iter_content(chunk_size=None))


def main():
    results = []
    passed = 0

    for i, tc in enumerate(TEST_CASES, 1):
        q = tc["question"]
        expected = tc["expected"]
        print(f"[{i:>2}/{len(TEST_CASES)}] {q}")

        try:
            answer = ask(q)
            ok = expected.replace(",", "") in answer.replace(",", "")
            status = "✅ PASS" if ok else "❌ FAIL"
            if ok:
                passed += 1
            print(f"         {status} | expected {expected} | got: {answer.strip()[:80]}")
        except Exception as e:
            answer = f"ERROR: {e}"
            status = "❌ ERROR"
            print(f"         {status} | {e}")

        results.append({
            "question": q,
            "expected": expected,
            "answer": answer,
            "pass": status.startswith("✅"),
        })

    print(f"\n{'='*50}")
    print(f"RESULT: {passed}/{len(TEST_CASES)} passed ({100*passed//len(TEST_CASES)}%)")
    print(f"{'='*50}")

    with open("eval_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("Results saved to eval_results.json")


if __name__ == "__main__":
    main()