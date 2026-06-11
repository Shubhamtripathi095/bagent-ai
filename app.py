import streamlit as st
import time

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# ======================
# STYLE
# ======================
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

h1, h2, h3, h4, p, label {
    color: #e2e8f0 !important;
}

input {
    background-color: #0f172a !important;
    color: white !important;
    border: 1px solid #38bdf8 !important;
}

button {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("""
<h1 style='text-align:center;'>🚀 BAGENT.AI</h1>
<h3 style='text-align:center;'>Autonomous Multi-Agent Business Analyst</h3>
""", unsafe_allow_html=True)

st.success("⚡ Discovery → Knowledge → Audit → User Story Generation")

st.markdown("---")

# ======================
# SESSION STATE
# ======================
if "output" not in st.session_state:
    st.session_state.output = ""

# ======================
# DOMAIN DETECTION
# ======================
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
    elif "hospital" in text or "patient" in text:
        return "Healthcare"
    elif "checkout" in text or "cart" in text:
        return "E-commerce"
    elif "employee" in text or "payroll" in text:
        return "HR"
    else:
        return "Generic"

# ======================
# LAYOUT
# ======================
left, right = st.columns([1.2, 0.8])

# ======================
# LEFT SIDE (INPUT)
# ======================
with left:
    st.subheader("🧠 Discovery Workspace")

    st.info("💡 Enter your business requirement in simple language")

    user_input = st.text_input(
        label="",
        placeholder="e.g. Build a banking fraud detection system"
    )

    if st.button("🚀 Generate User Story"):
        if user_input:

            progress = st.progress(0)

            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

            domain = detect_domain(user_input)

            output_text = (
                f"Domain: {domain}\n\n"
                f"User Story:\n"
                f"As a user,\n"
                f"I want to {user_input},\n"
                f"So that I achieve my goal.\n\n"
                f"Acceptance Criteria:\n"
                f"- Validate inputs\n"
                f"- Ensure security\n"
                f"- Handle errors\n\n"
                f"Gherkin Scenario:\n"
                f"Scenario: Successful execution\n"
                f"Given valid input\n"
                f"When system processes the request\n"
                f"Then success response is returned"
            )

            st.session_state.output = output_text

    st.markdown("### 📄 Generated Output")

    if st.session_state.output:
        st.code(st.session_state.output)
    else:
        st.warning("Output will appear here after generation")

# ======================
# RIGHT SIDE (AGENTS)
