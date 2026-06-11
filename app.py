import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI", layout="wide")

# =======================
# PREMIUM UI
# =======================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0f172a,#020617);
}
h1, h2, h3, p {
    color: white;
}

/* chat bubble */
[data-testid="stChatMessage"] {
    background-color: #111827;
    border-radius: 15px;
    padding: 12px;
    margin-bottom: 10px;
}

/* assistant */
[data-testid="stChatMessage"] > div:nth-child(2) {
    color: #e2e8f0;
}

/* input box */
textarea, input {
    background-color: #020617 !important;
    color: white !important;
    border: 1px solid #38bdf8 !important;
}
</style>
""", unsafe_allow_html=True)

# =======================
# HEADER
# =======================
st.markdown("# 🚀 BAGENT.AI")
st.caption("AI Copilot for Business Analysis")

# =======================
# SESSION STATE
# =======================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = ""

