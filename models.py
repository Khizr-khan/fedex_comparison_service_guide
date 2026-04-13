"""Pydantic request/response models for FastAPI."""

from typing import List, Optional
from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str       # "user" or "assistant"
    content: str


class AskRequest(BaseModel):
    question: str
    top_k: int = 5
    history: Optional[List[ChatMessage]] = []


class HealthResponse(BaseModel):
    status: str
    chunks_2026: int
    chunks_2025: int
    current_model: str


class SwitchModelRequest(BaseModel):
    model: str