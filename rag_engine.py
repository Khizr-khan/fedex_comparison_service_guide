"""
STEP 5 — Core RAG Engine
Handles retrieval, LLM inference, fallback chain, and 2025 vs 2026 comparison.
"""

import os
import re
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.documents import Document as Doc

# ── Config ────────────────────────────────────────────────────────────────────
CHROMA_DIR_2026 = "./chroma_fedex_db"
CHROMA_DIR_2025 = "./chroma_fedex_db_2025"
EMBED_MODEL = "all-MiniLM-L6-v2"

# ── LLM fallback chain (do not change order) ──────────────────────────────────
MODELS = {
    "llama-3.3-70b-versatile":                    {"limit": 100000, "label": "70B"},
    "meta-llama/llama-4-scout-17b-16e-instruct":  {"limit": 500000, "label": "Scout 17B"},
    "moonshotai/kimi-k2-instruct":                {"limit": 300000, "label": "Kimi K2"},
    "llama-3.1-8b-instant":                       {"limit": 500000, "label": "8B"},
}
MODEL_ORDER = list(MODELS.keys())

# ── Service keywords (sorted longest-first during detection) ──────────────────
SERVICE_KEYWORDS = {
    "ground and home delivery":       "FedEx Ground® and FedEx Home Delivery®",
    "ground & home delivery":         "FedEx Ground® and FedEx Home Delivery®",
    "international priority express": "FedEx International Priority® Express",
    "intl priority express":          "FedEx International Priority® Express",
    "international priority":         "FedEx International Priority®",
    "intl priority":                  "FedEx International Priority®",
    "international economy":          "FedEx International Economy®",
    "intl economy":                   "FedEx International Economy®",
    "international first":            "FedEx International First®",
    "intl first":                     "FedEx International First®",
    "international connect":          "FedEx® International Connect Plus",
    "intl connect":                   "FedEx® International Connect Plus",
    "connect plus":                   "FedEx® International Connect Plus",
    "priority overnight":             "FedEx Priority Overnight®",
    "first overnight":                "FedEx First Overnight®",
    "standard overnight":             "FedEx Standard Overnight®",
    "express saver":                  "FedEx Express Saver®",
    "home delivery":                  "FedEx Ground® and FedEx Home Delivery®",
    "2day a.m":                       "FedEx 2Day® A.M.",
    "2day am":                        "FedEx 2Day® A.M.",
    "2day":                           "FedEx 2Day®",
    "ground":                         "FedEx Ground® and FedEx Home Delivery®",
    " po ":                           "FedEx Priority Overnight®",
    " fo ":                           "FedEx First Overnight®",
    " so ":                           "FedEx Standard Overnight®",
}

SURCHARGE_SIGNALS = [
    "address correction", "saturday delivery", "saturday pickup",
    "on-call pickup", "automated pickup", "weekly pickup",
    "oversize", "oversize charge", "oversized",
    "dimensional weight", "fuel surcharge",
    "senseaware", "northern canada", "yukon", "nunavut",
    "northwest territories", "labrador", "metro service",
    "delivery manager", "date certain",
    "evening home delivery", "evening delivery", "home delivery evening",
    "signature required", "wrong address", "incorrect address",
    "bad address", "pickup fee", "pickup cost", "pickup charge",
    "deliver to a house", "residential delivery", "residential surcharge",
    "residential ground", "residential fee",
    "deliver to another address", "different address",
    "automated weekly", "weekly fee", "saturday on-call",
    "international ground", "northern surcharge",
    "extra for saturday", "extra saturday", "saturday fee",
    "extra charge for saturday", "saturday charge", "future day on-call",
    "senseaware fee", "senseaware cost",
    "rebill", "payer rebill", "overweight", "over weight",
    "dangerous goods", "hazmat", "inside delivery", "inside pickup",
    "remote area", "out of delivery area", "redirect", "reroute",
    "house delivery", "charge extra for house",
    "appointment home", "on demand care",
    "third party billing", "inbound processing",
    "controlled export", "signature proof",
    "ahs", "additional handling",
    "declared value", "declaration value","appointment"
]

COMPARISON_SIGNALS = [
    "compare", "last year", "previous year",
    "difference", "changed", "increase", "decrease",
    "vs", "versus", "new rate", "old rate",
    "what changed", "higher than", "lower than",
    "more expensive", "cheaper", "price change",
    "how much was", "what was the rate",
]

OUT_OF_SCOPE_SIGNALS = [
    "prohibited", "terms and conditions", "liability",
    "weather", "news", "politics", "joke", "recipe",
    "what time", "when does fedex open", "track my package",
    "where is my package",
]

# ── System prompts ────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are a FedEx 2026 rate and surcharge assistant.
Answer ONLY questions about FedEx 2026 list rates and surcharges.

RATE LOOKUP:
- Context chunks format: "Service: X. Shipping zone: Y. Package weight: Z lbs. Shipping rate: $R."
- Find the EXACT match for service, zone, and weight requested.
- State the rate in one sentence. Do NOT mention other weights or zones.
- If no exact match: "The exact rate is not available."

SURCHARGE LOOKUP:
- Find the fee in context and state it in ONE short sentence only.
- Format: "The [fee] is $X per package." — nothing more.
- Do NOT explain, do NOT add qualifications, do NOT mention other fees.
- Do NOT say "not available" if a dollar amount is visible in context.
- Adult Signature Required is always $10. Indirect/Direct Signature Required is always $7.60.
- For Additional Handling Surcharge (AHS), always ask which zone if not specified.
Never invent rates. Data from FedEx 2026 Service Guide, effective January 5, 2026.
"""

COMPARISON_PROMPT = """You are comparing FedEx shipping rates between 2025 and 2026.
You will be given context from both years labeled "2026 DATA" and "2025 DATA".

IMPORTANT: Present ONLY a simple 2-row table. Never create extra columns for zones.
If multiple zone rates exist, pick the most relevant one mentioned in the question.

| Year | Rate |
|------|------|
| 2026 | $X   |
| 2025 | $Y   |

Do NOT include difference, percentage, or commentary.
Do NOT add extra columns.
Just the table. Nothing else.
If a rate is missing, write "Not available" in the Rate column.
Never invent rates.
"""


class FedExRAG:
    def __init__(self):
        print("Loading FedEx RAG engine...")
        self.embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
        self.vectorstore_2026 = Chroma(
            persist_directory=CHROMA_DIR_2026,
            embedding_function=self.embeddings,
        )
        self.vectorstore_2025 = Chroma(
            persist_directory=CHROMA_DIR_2025,
            embedding_function=self.embeddings,
        )
        self.current_model = MODEL_ORDER[0]
        self.llm = self._make_llm(self.current_model)
        self.token_stats = {m: {"used": 0, "limit": MODELS[m]["limit"]} for m in MODELS}

        count_2026 = self.vectorstore_2026._collection.count()
        count_2025 = self.vectorstore_2025._collection.count()
        print(f"Ready. 2026: {count_2026} chunks, 2025: {count_2025} chunks.")

    # ── LLM helpers ───────────────────────────────────────────────────────────
    def _make_llm(self, model_name: str):
        return ChatGroq(
            model=model_name,
            api_key=os.environ.get("GROQ_API_KEY"),
            temperature=0,
            streaming=True,
        )

    def switch_model(self, model_name: str):
        self.current_model = model_name
        self.llm = self._make_llm(model_name)

    def _fallback_model(self):
        idx = MODEL_ORDER.index(self.current_model)
        if idx + 1 < len(MODEL_ORDER):
            return MODEL_ORDER[idx + 1]
        return None

    def _is_rate_limit_error(self, err: str) -> bool:
        return any(kw in err.lower() for kw in ["rate limit", "rate_limit", "429", "too many"])

    # ── Detectors ─────────────────────────────────────────────────────────────
    def _detect_service(self, question: str):
        padded = " " + question.lower() + " "
        for keyword in sorted(SERVICE_KEYWORDS.keys(), key=len, reverse=True):
            if keyword in padded:
                return SERVICE_KEYWORDS[keyword]
        return None

    def _detect_zone(self, question: str):
        q = question.lower()

        # Puerto Rico — stored as plain "Puerto Rico"
        if "puerto rico" in q:
            return "Puerto Rico"

        # Canada zones — stored as plain "Canada Zone A" in export sheet
        # (users asking about Canada rates want the outbound export rates)
        if "canada" in q:
            for letter, name in [("zone a", "Canada Zone A"), ("zone b", "Canada Zone B"), ("zone c", "Canada Zone C")]:
                if letter in q:
                    return name

        # International letter zones — stored as plain "Zone D" etc. in export sheet
        intl_letters = {
            "zone d": "Zone D", "zone e": "Zone E", "zone f": "Zone F",
            "zone g": "Zone G", "zone h": "Zone H", "zone i": "Zone I",
            "zone j": "Zone J", "zone k": "Zone K", "zone l": "Zone L",
            "zone m": "Zone M", "zone n": "Zone N", "zone o": "Zone O",
            "zone p": "Zone P",
        }
        for phrase in sorted(intl_letters.keys(), key=len, reverse=True):
            if phrase in q:
                return intl_letters[phrase]

        # Domestic numeric zones — stored as plain "Zone 3" etc.
        m = re.search(r"zone\s+(\d+)", q)
        return f"Zone {m.group(1)}" if m else None

    def _detect_weight(self, question: str):
        m = re.search(r"(\d+)\s*(?:lb|lbs|pound)", question.lower())
        return m.group(1) if m else None

    # ── Query classification ───────────────────────────────────────────────────
    def classify_query(self, question: str) -> str:
        q = question.lower()
        # Comparison checked FIRST — must contain BOTH a comparison signal AND a year reference
        if any(sig in q for sig in COMPARISON_SIGNALS):
            if "2025" in q or "2026" in q or "last year" in q or "previous year" in q:
                return "comparison"
        if any(sig in q for sig in SURCHARGE_SIGNALS):
            return "surcharge"
        if any(sig in q for sig in OUT_OF_SCOPE_SIGNALS):
            return "out_of_scope"
        rate_signals = [
            "rate", "price", "cost", "how much", "zone", "lbs", "lb",
            "pound", "weight", "overnight", "2day", "ground", "express",
            "priority", "saver", "economy", "freight", "shipping",
        ]
        if sum(1 for s in rate_signals if s in q) >= 2:
            return "rate"
        return "general"
    # ── DB retrieval with 3-retry loop ────────────────────────────────────────
    def _db_get(self, where_filter, vectorstore=None):
        vs = vectorstore or self.vectorstore_2026
        import time
        for attempt in range(7):
            try:
                raw = vs._collection.get(
                    where=where_filter,
                    include=["documents", "metadatas"],
                )
                if raw and raw["documents"]:
                    return [
                        Doc(page_content=d, metadata=m)
                        for d, m in zip(raw["documents"], raw["metadatas"])
                    ]
            except Exception:
                time.sleep(0.5)
                pass
        return []

    # ── 3-step cascading retrieval ─────────────────────────────────────────────
    def retrieve(self, question: str, query_type: str, top_k: int = 5, vectorstore=None):
        vs = vectorstore or self.vectorstore_2026

        if query_type == "surcharge":
            try:
                results = vs.similarity_search(
                    question,
                    k=top_k * 2,
                    filter={"type": {"$in": ["surcharge", "zone_text", "policy", "zone_overview"]}},
                )
                if results:
                    return results
            except Exception:
                pass
            return vs.similarity_search(question, k=top_k * 2)

        if query_type in ("rate", "general", "comparison"):
            service = self._detect_service(question)
            zone = self._detect_zone(question)
            weight = self._detect_weight(question)

            # Step 1: Exact 3-way match
            if service and zone and weight:
                docs = self._db_get(
                    {"$and": [
                        {"service": {"$eq": service}},
                        {"zone":    {"$eq": zone}},
                        {"weight":  {"$eq": weight}},
                    ]},
                    vs,
                )
                if service == "FedEx 2Day®":
                    docs = [d for d in docs if "A.M" not in d.page_content]
                if docs:
                    return docs[:3]

            # Step 2: Service + zone, let LLM pick weight
            if service and zone:
                docs = self._db_get(
                    {"$and": [
                        {"service": {"$eq": service}},
                        {"zone":    {"$eq": zone}},
                    ]},
                    vs,
                )
                if service == "FedEx 2Day®":
                    docs = [d for d in docs if "A.M" not in d.page_content]
                if docs:
                    return docs[:5]

            # Step 3: Service only, Python-filter for zone
            if service:
                docs = self._db_get({"service": {"$eq": service}}, vs)
                if service == "FedEx 2Day®":
                    docs = [d for d in docs if "A.M" not in d.page_content]
                if docs and zone:
                    zone_docs = [
                        d for d in docs
                        if d.metadata.get("zone") == zone
                    ]
                    if zone_docs:
                        if weight:
                            w_docs = [d for d in zone_docs if d.metadata.get("weight") == weight]
                            if w_docs:
                                return w_docs[:3]
                        return zone_docs[:5]
                if docs:
                    return docs[:5]

        return vs.similarity_search(question, k=top_k * 2)

    def retrieve_comparison(self, question: str):
        # Strip comparison signals to get the underlying query type
        # e.g. "Compare wrong address fee 2025 vs 2026" → classify as surcharge
        q_stripped = question.lower()
        for sig in COMPARISON_SIGNALS:
            q_stripped = q_stripped.replace(sig, "")

        # Classify the underlying question (rate or surcharge)
        if any(sig in q_stripped for sig in SURCHARGE_SIGNALS):
            underlying_type = "surcharge"
        else:
            underlying_type = "rate"

        docs_2026 = self.retrieve(question, underlying_type, top_k=8, vectorstore=self.vectorstore_2026)
        docs_2025 = self.retrieve(question, underlying_type, top_k=8, vectorstore=self.vectorstore_2025)
        return docs_2026, docs_2025

    # ── Token stats helpers ───────────────────────────────────────────────────
    def get_token_stats(self):
        return {
            "current_model": self.current_model,
            "models": self.token_stats,
        }

    # ── Main streaming method ─────────────────────────────────────────────────
    def ask_stream(self, question: str, top_k: int = 5, history: list = None):
        history = history or []

        if any(sig in question.lower() for sig in OUT_OF_SCOPE_SIGNALS):
            yield "I can only answer questions about FedEx 2026 list rates and surcharges."
            return

        # Short follow-up (≤5 words) → reuse last user question for retrieval
        q_words = question.strip().split()
        if len(q_words) <= 5 and history:
            last_user = next(
                (m["content"] for m in reversed(history) if m["role"] == "user"), None
            )
            retrieve_question = last_user if last_user else question
        else:
            retrieve_question = question.replace(" only", "").replace("only ", "")

        query_type = self.classify_query(retrieve_question)

        # Detect explicit year request → switch vectorstore
        q_lower = retrieve_question.lower()
        if "2025" in q_lower and query_type != "comparison":
            active_vs = self.vectorstore_2025
            active_system = SYSTEM_PROMPT.replace("2026", "2025")
        else:
            active_vs = self.vectorstore_2026
            active_system = SYSTEM_PROMPT

        if query_type == "comparison":
            docs_2026, docs_2025 = self.retrieve_comparison(retrieve_question)
            context_2026 = "\n".join([d.page_content for d in docs_2026[:5]])
            context_2025 = "\n".join([d.page_content for d in docs_2025[:5]])
            context = f"2026 DATA:\n{context_2026}\n\n2025 DATA:\n{context_2025}"
            system = COMPARISON_PROMPT
        else:
            docs = self.retrieve(retrieve_question, query_type, top_k=top_k, vectorstore=active_vs)
            docs = docs[:5]
            context = "\n".join([d.page_content for d in docs])
            system = active_system

        messages = [{"role": "system", "content": system}]
        for turn in history[-4:]:  # Last 4 turns
            messages.append({"role": turn["role"], "content": turn["content"]})
        messages.append({
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        })

        try:
            for chunk in self.llm.stream(messages):
                token = chunk.content
                if token:
                    self.token_stats[self.current_model]["used"] += 1
                    yield token
        except Exception as e:
            err = str(e)
            if self._is_rate_limit_error(err):
                fallback = self._fallback_model()
                if fallback:
                    self.switch_model(fallback)
                    yield f"\n[Switched to {MODELS[fallback]['label']}]\n\n"
                    for chunk in self.llm.stream(messages):
                        token = chunk.content
                        if token:
                            yield token
                else:
                    yield "All models are currently rate-limited. Please try again in a minute."
            else:
                yield f"Error: {err}"