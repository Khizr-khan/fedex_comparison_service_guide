"""
STEP 6 — FastAPI Backend
Exposes the FedEx RAG engine via REST API.
Runs on port 7860 for HuggingFace Spaces.
"""

import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from models import AskRequest, HealthResponse, SwitchModelRequest
from rag_engine import FedExRAG, MODELS

app = FastAPI(title="FedEx RAG API", version="1.0.0")

# ── CORS — required for Streamlit Cloud → HuggingFace ────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Load RAG engine once on startup ──────────────────────────────────────────
rag = FedExRAG()


# ── Endpoints ─────────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "FedEx RAG API running"}


@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(
        status="ok",
        chunks_2026=rag.vectorstore_2026._collection.count(),
        chunks_2025=rag.vectorstore_2025._collection.count(),
        current_model=rag.current_model,
    )


@app.post("/ask-stream")
def ask_stream(req: AskRequest):
    history = [{"role": m.role, "content": m.content} for m in (req.history or [])]

    def generator():
        for token in rag.ask_stream(
            question=req.question,
            top_k=req.top_k,
            history=history,
        ):
            yield token

    return StreamingResponse(generator(), media_type="text/plain")


@app.get("/token-stats")
def token_stats():
    return rag.get_token_stats()


@app.post("/switch-model")
def switch_model(req: SwitchModelRequest):
    if req.model not in MODELS:
        return {"error": f"Unknown model. Choose from: {list(MODELS.keys())}"}
    rag.switch_model(req.model)
    return {"switched_to": req.model, "label": MODELS[req.model]["label"]}


@app.get("/chunks-info")
def chunks_info():
    col_2026 = rag.vectorstore_2026._collection
    col_2025 = rag.vectorstore_2025._collection
    return {
        "2026": {
            "total": col_2026.count(),
        },
        "2025": {
            "total": col_2025.count(),
        },
    }


# ── Entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=7860, reload=False)