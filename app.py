import streamlit as st
import time

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# =====================
# CLEAN PROFESSIONAL STYLE
# =====================
st.markdown("""
<style>
body {
    background-color: #0b1220;
}

h1, h2, h3 {
    color: #e5e7eb;
}

.stChatMessage {
    border-radius: 12px;
}

textarea, input {
    background-color: #020617 !important;
    color: white !important;
}

/* Keep UI clean, no heavy styling */
</style>
""", unsafe_allow_html=True)

# =====================
# HEADER
# =====================
st.markdown("# 🚀 BAGENT.AI")
st.caption("AI Copilot for Business Analysis")

st.markdown("---")

# =====================
# SESSION STATE
# =====================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = ""

# =====================
# FIRST MESSAGE (IMPORTANT)
# =====================
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello — I'm your AI Business Analyst.\n\nDescribe what you want to build, and I’ll structure it professionally."
    })

# =====================
# DOMAIN DETECTION
# =====================
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
    if "hospital" in text or "patient" in text:
        return "Healthcare"
