"""
evaluate_aggressive2.py — 60 test cases (new data set):
  Section 1: 20 x 2026 tests (10 rates + 10 surcharges)
  Section 2: 20 x 2025 tests (10 rates + 10 surcharges)
  Section 3: 20 x comparison tests (10 rates + 10 surcharges)

Run: python evaluate_aggressive2.py
Requires uvicorn running on port 8000.
"""

import json
import requests

BACKEND = "http://localhost:8000"

# ── Section 1: 2026 Tests ─────────────────────────────────────────────────────
TESTS_2026 = [
    # 10 rate queries
    {"question": "Priority Overnight zone 3, 7 lbs",                       "expected": "91.26"},
    {"question": "Priority Overnight zone 6, 20 lbs",                      "expected": "267.36"},
    {"question": "First Overnight zone 2, 12 lbs",                         "expected": "109.16"},
    {"question": "First Overnight zone 8, 45 lbs",                         "expected": "578.96"},
    {"question": "Standard Overnight zone 3, 5 lbs",                       "expected": "68.95"},
    {"question": "Standard Overnight zone 6, 100 lbs",                     "expected": "916.00"},
    {"question": "2Day AM zone 7, 30 lbs",                                 "expected": "317.36"},
    {"question": "2Day zone 5, 15 lbs",                                    "expected": "108.11"},
    {"question": "Express Saver zone 4, 8 lbs",                            "expected": "41.11"},
    {"question": "Ground zone 4, 50 lbs",                                  "expected": "43.70"},
    # 10 surcharge queries
    {"question": "Saturday delivery fee",                                   "expected": "16.00"},
    {"question": "Oversize charge zones 5-6",                              "expected": "320.00"},
    {"question": "Address correction packages fee",                         "expected": "25.50"},
    {"question": "Adult signature required fee",                            "expected": "10.00"},
    {"question": "Weekly regularly scheduled pickup 5 days",               "expected": "35.50"},
    {"question": "Northern Canada Yukon surcharge 70 lbs or less",         "expected": "110.00"},
    {"question": "SenseAware domestic journey cost",                        "expected": "150.00"},
    {"question": "Home delivery date certain fee",                          "expected": "4.95"},
    {"question": "Dangerous goods international accessible surcharge",      "expected": "240.00"},
    {"question": "Delivery manager redirect within 120 miles",             "expected": "5.55"},
]

# ── Section 2: 2025 Tests ─────────────────────────────────────────────────────
TESTS_2025 = [
    # 10 rate queries
    {"question": "2025 Priority Overnight zone 3, 7 lbs",                  "expected": "84.59"},
    {"question": "2025 Priority Overnight zone 6, 20 lbs",                 "expected": "251.04"},
    {"question": "2025 First Overnight zone 2, 12 lbs",                    "expected": "104.12"},
    {"question": "2025 First Overnight zone 8, 45 lbs",                    "expected": "545.51"},
    {"question": "2025 Standard Overnight zone 3, 5 lbs",                  "expected": "64.20"},
    {"question": "2025 Standard Overnight zone 6, 100 lbs",                "expected": "876.00"},
    {"question": "2025 2Day AM zone 7, 30 lbs",                            "expected": "302.54"},
    {"question": "2025 2Day zone 5, 15 lbs",                               "expected": "101.51"},
    {"question": "2025 Express Saver zone 4, 8 lbs",                       "expected": "39.57"},
    {"question": "2025 Ground zone 4, 50 lbs",                             "expected": "41.42"},
    # 10 surcharge queries
    {"question": "2025 saturday delivery fee",                              "expected": "16.00"},
    {"question": "2025 oversize charge zones 5-6",                         "expected": "297.50"},
    {"question": "2025 address correction packages fee",                    "expected": "24.00"},
    {"question": "2025 adult signature required fee",                       "expected": "8.65"},
    {"question": "2025 weekly regularly scheduled pickup 5 days",          "expected": "35.50"},
    {"question": "2025 Northern Canada Yukon surcharge 70 lbs or less",    "expected": "105.00"},
    {"question": "2025 SenseAware domestic journey cost",                   "expected": "150.00"},
    {"question": "2025 home delivery date certain fee",                     "expected": "4.65"},
    {"question": "2025 dangerous goods international accessible surcharge", "expected": "240.00"},
    {"question": "2025 delivery manager redirect within 120 miles",        "expected": "5.55"},
]

# ── Section 3: Comparison Tests ───────────────────────────────────────────────
COMPARISON_TESTS = [
    # 10 rate comparisons
    {
        "question":      "Compare Priority Overnight zone 3, 7 lbs 2025 vs 2026",
        "label":         "Priority Overnight zone 3, 7 lbs",
        "expected_2026": "91.26",
        "expected_2025": "84.59",
    },
    {
        "question":      "Compare First Overnight zone 8, 45 lbs 2025 vs 2026",
        "label":         "First Overnight zone 8, 45 lbs",
        "expected_2026": "578.96",
        "expected_2025": "545.51",
    },
    {
        "question":      "Compare Standard Overnight zone 6, 100 lbs 2025 vs 2026",
        "label":         "Standard Overnight zone 6, 100 lbs",
        "expected_2026": "916.00",
        "expected_2025": "876.00",
    },
    {
        "question":      "Compare 2Day AM zone 7, 30 lbs 2025 vs 2026",
        "label":         "2Day AM zone 7, 30 lbs",
        "expected_2026": "317.36",
        "expected_2025": "302.54",
    },
    {
        "question":      "Compare 2Day zone 5, 15 lbs 2025 vs 2026",
        "label":         "2Day zone 5, 15 lbs",
        "expected_2026": "108.11",
        "expected_2025": "101.51",
    },
    {
        "question":      "Compare Ground zone 4, 50 lbs 2025 vs 2026",
        "label":         "Ground zone 4, 50 lbs",
        "expected_2026": "43.70",
        "expected_2025": "41.42",
    },
    {
        "question":      "Compare Intl Priority zone G, 60 lbs 2025 vs 2026",
        "label":         "Intl Priority zone G, 60 lbs",
        "expected_2026": "1237.60",
        "expected_2025": "1162.10",
    },
    {
        "question":      "Compare Intl First zone F, 25 lbs 2025 vs 2026",
        "label":         "Intl First zone F, 25 lbs",
        "expected_2026": "572.89",
        "expected_2025": "540.38",
    },
    {
        "question":      "Compare Intl Economy Puerto Rico, 15 lbs 2025 vs 2026",
        "label":         "Intl Economy Puerto Rico, 15 lbs",
        "expected_2026": "152.65",
        "expected_2025": "143.90",
    },
    {
        "question":      "Compare Intl Priority zone L, 70 lbs 2025 vs 2026",
        "label":         "Intl Priority zone L, 70 lbs",
        "expected_2026": "2564.03",
        "expected_2025": "2409.84",
    },
    # 10 surcharge comparisons
    {
        "question":      "Compare saturday delivery fee 2025 vs 2026",
        "label":         "Saturday delivery fee",
        "expected_2026": "16.00",
        "expected_2025": "16.00",
    },
    {
        "question":      "Compare oversize charge zones 5-6 2025 vs 2026",
        "label":         "Oversize charge zones 5-6",
        "expected_2026": "320.00",
        "expected_2025": "297.50",
    },
    {
        "question":      "Compare address correction packages fee 2025 vs 2026",
        "label":         "Address correction packages fee",
        "expected_2026": "25.50",
        "expected_2025": "24.00",
    },
    {
        "question":      "Compare adult signature required fee 2025 vs 2026",
        "label":         "Adult Signature Required fee",
        "expected_2026": "10.00",
        "expected_2025": "8.65",
    },
    {
        "question":      "Compare SenseAware domestic journey cost 2025 vs 2026",
        "label":         "SenseAware domestic journey cost",
        "expected_2026": "150.00",
        "expected_2025": "150.00",
    },
    {
        "question":      "Compare Northern Canada Yukon surcharge 2025 vs 2026",
        "label":         "Northern Canada Yukon surcharge",
        "expected_2026": "110.00",
        "expected_2025": "105.00",
    },
    {
        "question":      "Compare home delivery date certain fee 2025 vs 2026",
        "label":         "Home delivery date certain fee",
        "expected_2026": "4.95",
        "expected_2025": "4.65",
    },
    {
        "question":      "Compare delivery manager redirect within 120 miles 2025 vs 2026",
        "label":         "Delivery manager redirect within 120 miles",
        "expected_2026": "5.55",
        "expected_2025": "5.55",
    },
    {
        "question":      "Compare Connect Plus zone K, 55 lbs 2025 vs 2026",
        "label":         "Connect Plus zone K, 55 lbs",
        "expected_2026": "1138.43",
        "expected_2025": "1077.04",
    },
    {
        "question":      "Compare Express Saver zone 4, 8 lbs 2025 vs 2026",
        "label":         "Express Saver zone 4, 8 lbs",
        "expected_2026": "41.11",
        "expected_2025": "39.57",
    },
]


def ask(question: str) -> str:
    resp = requests.post(
        f"{BACKEND}/ask-stream",
        json={"question": question, "top_k": 5, "history": []},
        stream=True,
        timeout=60,
    )
    return "".join(chunk.decode() for chunk in resp.iter_content(chunk_size=None))


def normalize(s: str) -> str:
    return s.replace(",", "").replace("$", "").strip()


def run_section(title, tests, section_type="single"):
    print(f"\n{'=' * 60}")
    print(f"{title}")
    print(f"{'=' * 60}")
    results = []
    passed = 0

    for i, tc in enumerate(tests, 1):
        q = tc["question"]

        if section_type == "single":
            expected = tc["expected"]
            print(f"[{i:>2}/{len(tests)}] {q}")
            try:
                answer = ask(q)
                ok = normalize(expected) in normalize(answer)
                status = "✅ PASS" if ok else "❌ FAIL"
                if ok:
                    passed += 1
                print(f"         {status} | expected {expected} | got: {answer.strip()[:80]}")
            except Exception as e:
                answer, status = f"ERROR: {e}", "❌ ERROR"
                print(f"         {status} | {e}")
            results.append({"question": q, "expected": expected,
                            "answer": answer, "pass": status.startswith("✅")})

        else:
            exp_2026 = tc["expected_2026"]
            exp_2025 = tc["expected_2025"]
            label = tc["label"]
            print(f"[{i:>2}/{len(tests)}] {label}")
            try:
                answer = ask(q)
                norm = normalize(answer)
                has_2026 = normalize(exp_2026) in norm
                has_2025 = normalize(exp_2025) in norm
                ok = has_2026 and has_2025
                if ok:
                    passed += 1
                    status = "✅ PASS"
                elif has_2026 and not has_2025:
                    status = "⚠️  PARTIAL (2026 ✅  2025 ❌)"
                elif has_2025 and not has_2026:
                    status = "⚠️  PARTIAL (2025 ✅  2026 ❌)"
                else:
                    status = "❌ FAIL"
                print(f"         {status} | 2026: {exp_2026} | 2025: {exp_2025}")
                print(f"         got: {answer.strip()[:100]}")
            except Exception as e:
                answer, status = f"ERROR: {e}", "❌ ERROR"
                print(f"         {status} | {e}")
            results.append({"question": q, "expected_2026": exp_2026,
                            "expected_2025": exp_2025, "answer": answer,
                            "pass": status.startswith("✅")})

    print(f"\n{title}: {passed}/{len(tests)} passed")
    return results, passed


def main():
    all_results = []

    r1, p1 = run_section("SECTION 1 — 2026 Tests (10 rates + 10 surcharges)", TESTS_2026, "single")
    r2, p2 = run_section("SECTION 2 — 2025 Tests (10 rates + 10 surcharges)", TESTS_2025, "single")
    r3, p3 = run_section("SECTION 3 — Comparison Tests (10 rates + 10 surcharges)", COMPARISON_TESTS, "comparison")

    all_results.extend(r1 + r2 + r3)
    total = len(TESTS_2026) + len(TESTS_2025) + len(COMPARISON_TESTS)
    total_passed = p1 + p2 + p3

    print(f"\n{'=' * 60}")
    print(f"FINAL RESULT: {total_passed}/{total} passed ({100 * total_passed // total}%)")
    print(f"  2026 Tests   : {p1}/{len(TESTS_2026)}")
    print(f"  2025 Tests   : {p2}/{len(TESTS_2025)}")
    print(f"  Comparisons  : {p3}/{len(COMPARISON_TESTS)}")
    print(f"{'=' * 60}")

    with open("eval_aggressive2_results.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print("Results saved to eval_aggressive2_results.json")


if __name__ == "__main__":
    main()