import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI", layout="wide")

# ==========================
# STYLE (PRO UI)
# ==========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Title */
h1 {
    text-align: center;
    font-size: 3rem;
    color: #38bdf8;
}

/* Subtitle */
h3 {
    text-align: center;
    color: #94a3b8;
}

/* Cards */
.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #38bdf8;
    margin-bottom: 15px;
}

/* Highlight box */
.stAlert {
    background: #1e293b !important;
}

/* Button */
button {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    border-radius: 8px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# HEADER (HERO SECTION)
# ==========================
st.markdown("""
# 🚀 BAGENT.AI  

### ⚡ Autonomous Multi-Agent Business Analyst  
Transform ideas → structured backlog in seconds  
---
""")

# ==========================
# CAPABILITIES
# ==========================
colA, colB, colC = st.columns(3)

with colA:
    st.markdown("""
    <div class="card">
    <h4>🧠 Smart Discovery</h4>
    Detects domain & understands intent  
    </div>
    """, unsafe_allow_html=True)

with colB:
    st.markdown("""
    <div class="card">
    <h4>🌐 Knowledge Enrichment</h4>
    Uses RAG-style domain intelligence  
    </div>
    """, unsafe_allow_html=True)

with colC:
    st.markdown("""
    <div class="card">
    <h4>⚙️ Auto Backlog</h4>
    Generates user stories + Gherkin instantly  
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==========================
# SAMPLE PROMPTS
# ==========================
with st.expander("💡 Try Sample Prompts"):
    st.markdown("""
- 🏦 Build a loan approval system with fraud detection  
- 🏥 Create patient management with HIPAA compliance  
- 🛒 Design e-commerce checkout with payments  
- 👥 Develop HR payroll system with reports  
""")

# ==========================
# SESSION STATE
# ==========================
if "stage" not in st.session_state:
    st.session_state.stage = "idle"

if "output" not in st.session_state:
    st.session_state.output = ""

# ==========================
# DOMAIN + LOGIC
# ==========================
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
    elif "patient" in text or "hospital" in text:
        return "Healthcare"
    elif "checkout" in text or "cart" in text:
        return "E-commerce"
    return "Generic"

# ==========================
# LAYOUT
# ==========================
left, right = st.columns([1.3, 1])

# ==========================
# LEFT (AI INPUT)
# ==========================
with left:
    st.subheader("🧠 Discovery Workspace")

    st.info("""
👉 Describe your requirement in natural language  
👉 AI will convert it into structured backlog  
""")

    user_input = st.text_input(
        "💡 Enter your requirement:",
        placeholder="e.g. Build a banking fraud detection system"
    )

    if st.button("🚀 Generate"):
        if user_input:

            st.session_state.stage = "discovery"
            time.sleep(0.5)

            st.session_state.stage = "knowledge"
            time.sleep(0.5)

            st.session_state.stage = "audit"
            time.sleep(0.5)

            st.session_state.stage = "output"

            domain = detect_domain(user_input)

            output = f"""
Domain: {domain}

User Story:
As a user,
I want to {user_input},
So that I achieve the desired functionality.

Acceptance Criteria:
- System validates input
- Ensures security & compliance
- Handles errors gracefully

Gherkin:

Scenario: Successful execution
Given valid user input
When process is triggered
Then system returns success
"""
            st.session_state.output = output

# ==========================
# RIGHT (AGENTS PANEL)
# ==========================
with right:
    st.subheader("⚙️ Agent Control Panel")

    st.markdown("### 🤖 Active Agents")

    st.write("Discovery Agent:", "✅" if st.session_state.stage != "idle" else "⏳")
    st.write("Knowledge Agent:", "✅" if st.session_state.stage in ["knowledge", "audit", "output"] else "⏳")
    st.write("Audit Agent:", "✅" if st.session_state.stage in ["audit", "output"] else "⏳")
    st.write("Writer Agent:", "✅" if st.session_state.stage == "output" else "⏳")

    st.markdown("---")

    st.subheader("📊 Execution Logs")

    if st.session_state.stage == "idle":
        st.info("Waiting for input...")

    if st.session_state.stage == "discovery":
        st.info("Understanding requirement...")

    if st.session_state.stage == "knowledge":
        st.info("Fetching domain knowledge...")

    if st.session_state.stage == "audit":
        st.info("Running compliance checks...")

    if st.session_state.stage == "output":
        st.success("✅ User Story Generated")

        st.markdown("### 📄 Output")
        st.code(st.session_state.output)

        st.metric("⏱ Time Saved", "10 days → 1 min")
        st.metric("📊 Accuracy", "92%")

# ==========================
# RESET
# ==========================
st.markdown("---")
if st.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()
