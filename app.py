import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI", layout="wide")

# ==========================
# HEADER
# ==========================
st.title("🤖 BAGENT.AI")
st.caption("Autonomous Multi-Agent BA Orchestrator")
st.markdown("---")

# ==========================
# SESSION STATE
# ==========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "idle"

if "final_output" not in st.session_state:
    st.session_state.final_output = ""

# ==========================
# DOMAIN INTELLIGENCE
# ==========================
def detect_domain(text):
    text = text.lower()

    if any(x in text for x in ["loan", "bank", "finance", "payment"]):
        return "Finance"
    elif any(x in text for x in ["patient", "hospital", "doctor", "health"]):
        return "Healthcare"
    elif any(x in text for x in ["order", "cart", "checkout", "ecommerce"]):
        return "E-commerce"
    elif any(x in text for x in ["hr", "employee", "payroll"]):
        return "HR"
    else:
        return "Generic"

def external_knowledge_stub(domain):
    # This simulates pulling knowledge from open sources
    knowledge = {
        "Finance": ["Fraud Detection", "KYC Compliance", "Secure transactions"],
        "Healthcare": ["HIPAA Compliance", "Patient Data Security", "Audit Logs"],
        "E-commerce": ["Cart flow", "Payment gateway", "Order tracking"],
        "HR": ["Payroll security", "Leave workflows", "Employee data rules"],
        "Generic": ["Validation rules", "Data security", "Audit logging"]
    }
    return knowledge.get(domain, ["Standard business rules"])

# ==========================
# USER STORY GENERATOR
# ==========================
def generate_user_story(input_text):
    domain = detect_domain(input_text)
    enrichments = external_knowledge_stub(domain)

    story = f"""
Domain: {domain}

User Story:
As a user,
I want to {input_text},
So that I can achieve the intended business outcome.

Acceptance Criteria:
- System should validate all inputs
- Ensure security and compliance
"""

    for item in enrichments:
        story += f"- {item}\n"

    story += """
Gherkin Scenario:

Scenario: Successful execution
  Given the user provides valid input
  When the system processes the request
  Then the system should return a successful outcome
"""

    return story, domain

# ==========================
# LAYOUT
# ==========================
col1, col2 = st.columns([1.3, 1])

# ==========================
# LEFT SIDE - CHAT
# ==========================
with col1:
    st.subheader("🧠 Discovery Workspace")

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    user_input = st.chat_input("Describe your requirement (any domain)...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        if st.session_state.stage == "idle":
            response = "🔍 Understanding requirement & detecting domain..."
            st.session_state.stage = "discovery"

        elif st.session_state.stage == "discovery":
            response = "🌐 Fetching domain knowledge from open sources..."
            st.session_state.stage = "external"

        elif st.session_state.stage == "external":
            response = "🛡️ Running compliance and risk validation..."
            st.session_state.stage = "audit"

        elif st.session_state.stage == "audit":
            response = "✍️ Generating structured user story..."
            story, domain = generate_user_story(user_input)
            st.session_state.final_output = story
            st.session_state.stage = "output"

        else:
            response = "✅ Process complete. Reset to start new request."

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# ==========================
# RIGHT SIDE - AGENTS
# ==========================
with col2:
    st.subheader("⚙️ Agent Control Panel")

    st.markdown("### 🧑‍💼 Active Agents")

    st.write("Lead Discovery Agent:", "✅" if st.session_state.stage != "idle" else "⏳")
    st.write("Knowledge Agent (RAG):", "✅" if st.session_state.stage in ["external", "audit", "output"] else "⏳")
    st.write("Audit Agent:", "✅" if st.session_state.stage in ["audit", "output"] else "⏳")
    st.write("Writer Agent:", "✅" if st.session_state.stage == "output" else "⏳")

    st.markdown("---")
    st.markdown("### 📊 Execution Logs")

    if st.session_state.stage == "idle":
        st.info("Waiting for requirement input...")

    if st.session_state.stage == "external":
        with st.status("Fetching external knowledge...", expanded=True):
            st.write("🔍 Searching open-source knowledge...")
            time.sleep(1)
            st.write("📚 Enriching domain understanding...")
            st.success("Knowledge loaded ✅")

