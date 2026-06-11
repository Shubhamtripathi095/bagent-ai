import streamlit as st
import time

# CONFIG
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# SAFE CSS (no broken triple quotes)
st.markdown(
"""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

h1, h2, h3, h4, p {
    color: #e2e8f0 !important;
}

input {
    background-color: #0f172a !important;
    color: white !important;
}

button {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
}
</style>
""",
unsafe_allow_html=True
)

# HEADER
st.markdown(
"""
<h1 style='text-align:center;'>🚀 BAGENT.AI</h1>
<h3 style='text-align:center;'>Autonomous Multi-Agent Business Analyst</h3>
""",
unsafe_allow_html=True
)

st.success("⚡ Discovery → Knowledge → Audit → User Story Generation")

st.markdown("---")

# STATE
if "output" not in st.session_state:
    st.session_state.output = ""

# DOMAIN DETECTION
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
    elif "patient" in text or "hospital" in text:
        return "Healthcare"
    elif "checkout" in text:
        return "E-commerce"
    return "Generic"

# LAYOUT
left, right = st.columns([1.2, 0.8])

# LEFT SIDE
with left:
    st.subheader("🧠 Discovery Workspace")

    user_input = st.text_input(
