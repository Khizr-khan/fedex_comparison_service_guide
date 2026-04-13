"""
STEP 7 — Streamlit Frontend
Chat interface with streaming, model selector, and example questions.
"""

import requests
import streamlit as st

# BACKEND_URL = "http://localhost:8000"
BACKEND_URL = "https://khizr72-fedex-comparison-service-guide.hf.space"

EXAMPLE_QUESTIONS = [
    "Priority Overnight zone 4, 10 lbs",
    "First Overnight zone 7, 3 lbs",
    "Standard Overnight zone 5, 30 lbs",
    "2Day zone 6, 40 lbs",
    "2Day AM zone 7, 75 lbs",
    "Express Saver zone 8, 5 lbs",
    "Ground zone 3, 20 lbs",
    "Intl Economy Puerto Rico, 101 lbs",
    "Intl Priority zone D, 81 lbs",
    "Intl First Canada zone A, 59 lbs",
    "Intl Priority Express zone J, 91 lbs",
    "Connect Plus zone F, 97 lbs",
    "Wrong address fee",
    "Saturday delivery fee Priority Overnight",
    "Adult signature required fee",
    "Automated weekly pickup cost",
    "Yukon 50lb international ground surcharge",
    "Redirect package within 120 miles fee",
    "Senseaware domestic journey cost",
    "Compare Priority Overnight zone 4, 10 lbs 2025 vs 2026",
]

MODELS = [
    "llama-3.3-70b-versatile",
    "meta-llama/llama-4-scout-17b-16e-instruct",
    "moonshotai/kimi-k2-instruct",
    "llama-3.1-8b-instant",
]

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FedEx AI Shipping Consultant",
    page_icon="📦",
    layout="wide",
)

st.title("📦 FedEx AI Shipping Consultant")
st.caption("Ask about FedEx 2026 list rates, surcharges, or compare 2025 vs 2026 rates.")

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Settings")

    selected_model = st.selectbox("LLM Model", MODELS, index=0)
    if st.button("Switch Model"):
        try:
            resp = requests.post(
                f"{BACKEND_URL}/switch-model",
                json={"model": selected_model},
                timeout=10,
            )
            if resp.ok:
                st.success(f"Switched to {resp.json().get('label', selected_model)}")
            else:
                st.error("Failed to switch model")
        except Exception as e:
            st.error(f"Backend error: {e}")

    st.divider()

    # Health check
    try:
        health = requests.get(f"{BACKEND_URL}/health", timeout=5).json()
        st.success(f"✅ API Online")
        st.caption(f"2026 chunks: {health.get('chunks_2026', '?')}")
        st.caption(f"2025 chunks: {health.get('chunks_2025', '?')}")
        st.caption(f"Model: {health.get('current_model', '?')[:30]}")
    except Exception:
        st.error("❌ API Offline")

    st.divider()
    st.header("💡 Example Questions")
    for q in EXAMPLE_QUESTIONS:
        if st.button(q, key=f"ex_{q}"):
            st.session_state.pending_question = q

    st.divider()
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ── Display chat history ──────────────────────────────────────────────────────
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ── Handle example question click ────────────────────────────────────────────
user_input = st.chat_input("Ask about FedEx 2026 rates or surcharges...")

if st.session_state.pending_question:
    user_input = st.session_state.pending_question
    st.session_state.pending_question = None

# ── Handle input ──────────────────────────────────────────────────────────────
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""

        try:
            history_payload = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages[:-1]  # exclude current user msg
            ]

            with requests.post(
                f"{BACKEND_URL}/ask-stream",
                json={
                    "question": user_input,
                    "top_k": 5,
                    "history": history_payload,
                },
                stream=True,
                timeout=60,
            ) as resp:
                resp.raise_for_status()
                for chunk in resp.iter_content(chunk_size=None):
                    if chunk:
                        token = chunk.decode("utf-8")
                        full_response += token
                        placeholder.markdown(full_response + "▌")

            placeholder.markdown(full_response)

        except requests.exceptions.ConnectionError:
            full_response = "❌ Cannot connect to backend. Please check the API URL."
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"❌ Error: {str(e)}"
            placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})