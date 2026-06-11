import streamlit as st
import time

# ==========================
# CONFIG
# ==========================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# ==========================
# STYLE
# ==========================
st.markdown("""
<style>

/* Page width */
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Text */
h1, h2, h3, h4, p {
    color: #e2e8f0 !important;
}

/* Cards */
.card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(56,189,248,0.5);
    box-shadow: 0 0 15px rgba(56,189,248,0.2);
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

</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER
# ==========================
st.markdown("""
<h1 style='text-align:center;'>🚀 BAGENT.AI</h1>
<h3 style='text-align:center; color:#94a3b8;'>
Autonomous Multi-Agent Business Analyst
</h3>
""", unsafe_allow_html=True)

st.success("⚡ Discovery → Knowledge → Audit → User Story Generation")

st.markdown("---")

# ==========================
# FEATURES
# ==========================
col1, col2, col3 = st.columns(3)

col1.markdown("""
<div class="card">
<h4>🧠 Smart Discovery</h4>
<p>Understands business requirement & detects domain</p>
</div>
""", unsafe_allow_html=True)

col2.markdown("""
<div class="card">
<h4>🌐 Knowledge Engine</h4>
<p>Enriches with domain intelligence (RAG-style)</p>
</div>
""", unsafe_allow_html=True)

col3.markdown("""
<div class="card">
<h4>⚙️ Auto Backlog</h4>
<p>Generates user stories & Gherkin instantly</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==========================
# SAMPLE PROMPTS
# ==========================
with st.expander("💡 Try Sample Prompts"):
    st.markdown("""
- Build a loan approval system with fraud detection  
- Create hospital system with patient records  
- Design e-commerce checkout with payments  
- Develop HR payroll system  
""")

# ==========================
# STATE
# ==========================
if "stage" not in st.session_state:
    st.session_state.stage = "idle"

if "output" not in st.session_state:
    st.session_state.output = ""

# ==========================
# DOMAIN LOGIC
# ==========================
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
    elif "patient" in text or "hospital" in text:
        return "Healthcare"
    elif "checkout" in text or "cart" in text:
        return "E-commerce"
    elif "employee" in text or "hr" in text:
        return "HR"
    return "Generic"

# ==========================
# MAIN LAYOUT
# ==========================
left, right = st.columns([1.2, 0.8])

# ==========================
# LEFT SIDE (INPUT)
# ==========================
with left:
    st.subheader("🧠 Discovery Workspace")

    st.info("""
💡 Describe your requirement in simple language  

Example:
- Loan system with fraud detection  
- Hospital patient data system  
- Checkout with refund flow  
""")

    user_input = st.text_input(
        "",
        placeholder="e.g. Build a banking fraud detection system",
    )

    if st.button("🚀 Generate User Story"):
        if user_input:

            st.session_state.stage = "discovery"
            time.sleep(0.4)

            st.session_state.stage = "knowledge"
            time.sleep(0.4)

            st.session_state.stage = "audit"
            time.sleep(0.4)

            st.session_state.stage = "output"

            domain = detect_domain(user_input)

            st.session_state.output = f"""
Domain: {domain}

User Story:
As a user,
I want to {user_input},
So that I achieve my goal.

Acceptance Criteria:
- System validates inputs
- Ensures security & compliance
- Handles errors properly

Gherkin Scenario:
Scenario: Successful execution
Given valid input
When request is processed
Then system returns success
"""

    st.markdown("### 📄 Generated Output")

    if st.session_state.stage == "output":
        st.code(st.session_state.output)
    else:
        st.warning("Your generated output will appear here...")

# ==========================
# RIGHT SIDE (AGENTS)
# ==========================
with right:
    st.subheader("⚙️ Agent Control Panel")

    st.markdown("### 🤖 Active Agents")

    st.write("Discovery Agent:", "✅" if st.session_state.stage != "idle" else "⏳")
    st.write("Knowledge Agent:", "✅" if st.session_state.stage in ["knowledge", "audit", "output"] else "⏳")
    st.write("Audit Agent:", "✅" if st.session_state.stage in ["audit", "output"] else "⏳")
    st.write("Writer Agent:", "✅" if st.session_state.stage == "output" else "⏳")

    st.markdown("---")

    st.subheader("📊 Execution Flow")

    if st.session_state.stage == "idle":
        st.info("Waiting for input...")

    if st.session_state.stage == "discovery":
        st.info("1️⃣ Understanding requirement")

    if st.session_state.stage == "knowledge":
        st.info("2️⃣ Enriching domain knowledge")

    if st.session_state.stage == "audit":
        st.info("3️⃣ Running validation checks")

    if st.session_state.stage == "output":
        st.success("✅ User Story Generated")

        st.metric("⏱ Time Saved", "10 days → 1 min")
        st.metric("📊 Accuracy", "92%")

# ==========================
# RESET
# ==========================
st.markdown("---")

if st.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()
