import streamlit as st
import time

# ==========================
# CONFIG
# ==========================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# ==========================
# STYLE (FIXED CLEAN UI)
# ==========================
st.markdown("""
<style>

/* Page width fix */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Text visibility */
h1, h2, h3, h4, p, label {
    color: #e2e8f0 !important;
}

/* Cards */
.card {
    background: #1e293b;
    padding: 16px;
    border-radius: 10px;
    border: 1px solid rgba(56,189,248,0.4);
    margin-bottom: 10px;
}

/* Input */
input {
    background-color: #0f172a !important;
    color: white !important;
}

/* Button */
button {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    border-radius: 8px;
}

/* Logs box */
.stAlert {
    background: #1e293b !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown("""
<h1>🚀 BAGENT.AI</h1>
<h3>Autonomous Multi-Agent Business Analyst</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================
# CAPABILITIES
# ==========================
col1, col2, col3 = st.columns(3)

col1.markdown('<div class="card">🧠 Detects domain & understands requirement</div>', unsafe_allow_html=True)
col2.markdown('<div class="card">🌐 Enriches knowledge (RAG-style)</div>', unsafe_allow_html=True)
col3.markdown('<div class="card">⚙️ Generates User Stories & Gherkin</div>', unsafe_allow_html=True)

st.markdown("---")

# ==========================
# SAMPLE PROMPTS
# ==========================
with st.expander("💡 Try Sample Prompts"):
    st.markdown("""
- Build a **loan approval system with fraud detection**
- Create a **hospital patient management system**
- Design an **e-commerce checkout flow**
- Develop an **HR payroll system**
""")

# ==========================
# SESSION STATE
# ==========================
if "stage" not in st.session_state:
    st.session_state.stage = "idle"

if "output" not in st.session_state:
    st.session_state.output = ""

# ==========================
# DOMAIN DETECTION
# ==========================
def detect_domain(text):
    text = text.lower()
    if any(x in text for x in ["loan", "bank", "finance"]):
        return "Finance"
    elif any(x in text for x in ["hospital", "patient", "health"]):
        return "Healthcare"
    elif any(x in text for x in ["checkout", "cart", "order"]):
        return "E-commerce"
    elif any(x in text for x in ["employee", "hr", "payroll"]):
        return "HR"
    return "Generic"

# ==========================
# MAIN LAYOUT
# ==========================
left, right = st.columns([1.1, 0.9], gap="large")

# ==========================
# LEFT SIDE
# ==========================
with left:
    st.subheader("🧠 Discovery Workspace")

    st.info("""
👉 Describe any business requirement  
👉 BAGENT.AI converts it into structured backlog  
""")

    user_input = st.text_input(
        "",
        placeholder="e.g. Build a banking fraud detection system",
    )

    if st.button("🚀 Generate User Story"):
        if user_input:

            st.session_state.stage = "discovery"
            time.sleep(0.5)

            st.session_state.stage = "knowledge"
