import streamlit as st
import time

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# =====================
# HEADER
# =====================
st.title("🚀 BAGENT.AI")
st.caption("AI Copilot for Business Analysis")
st.markdown("---")

# =====================
# SESSION STATE
# =====================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello — I’m your AI Business Analyst.\n\nDescribe a system and I will help structure it."
        }
    ]

if "context" not in st.session_state:
    st.session_state.context = ""

# =====================
# DOMAIN DETECTION
# =====================
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
