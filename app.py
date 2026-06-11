import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI", layout="wide")

# =========================
# HEADER
# =========================
st.title("🚀 BAGENT.AI")
st.caption("AI Copilot for Business Analysis")
st.markdown("---")

# =========================
# STATE INIT (IMPORTANT)
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello — I’m your AI Business Analyst.\n\nDescribe a system and I will convert it into structured requirements."
        }
    ]

if "context" not in st.session_state:
    st.session_state.context = ""

# =========================
# DOMAIN DETECTION
# =========================
def detect_domain(text):
    t = text.lower()
    if "loan" in t or "bank" in t:
        return "Finance"
    if "hospital" in t or "patient" in t:
        return "Healthcare"
    if "checkout" in t or "cart" in t:
        return "E-commerce"
    return "General"

# =========================
# RESPONSE LOGIC
# =========================
def generate_response(user_input):
    t = user_input.lower()

    if t in ["hi", "hello"]:
