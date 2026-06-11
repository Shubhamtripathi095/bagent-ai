import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI ELITE", layout="wide")

# =========================
# HEADER
# =========================
st.title("🚀 BAGENT.AI ELITE")
st.caption("Conversational Multi-Agent AI Business Analyst")

st.markdown("---")

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = ""

# =========================
# DOMAIN DETECTION
# =========================
def detect_domain(text):
    text = text.lower()
    if "loan" in text or "bank" in text:
        return "Finance"
    if "hospital" in text or "patient" in text:
        return "Healthcare"
    if "checkout" in text or "cart" in text:
        return "E-commerce"
    if "employee" in text:
        return "HR"
    return "Generic"

# =========================
# KNOWLEDGE BASE
# =========================
knowledge_base = {
    "Finance": ["KYC compliance", "Fraud detection", "Secure transactions"],
    "Healthcare": ["HIPAA compliance", "Patient data security"],
    "E-commerce": ["Cart flow", "Payment integration"],
    "HR": ["Payroll rules", "Employee data security"],
    "Generic": ["Validation checks", "Security rules"]
}

# =========================
# AI RESPONSE LOGIC
# =========================
def generate_response(user_input):

    # conversational handling
    text = user_input.lower()

    if text in ["hi", "hello", "hey"]:
        return "👋 Hello! Tell me what system you'd like to build."

    if "wow" in text:
        return "😄 Glad you liked it! Try refining your requirement."

    if "thank" in text:
        return "🙏 You're welcome! Ask anything else."

    # context
    st.session_state.context += " " + user_input

    domain = detect_domain(st.session_state.context)
    knowledge = knowledge_base[domain]

    return domain, knowledge, st.session_state.context


# =========================
# OUTPUT BUILDER
# =========================
def build_output(domain, knowledge, combined):

    text = f"""
🧠 **Understanding**
This is a {domain} system with core business logic.

📌 **User Story**
As a user,
I want to {combined},
So that I achieve my goal.

✅ **Acceptance Criteria**
"""
    for k in knowledge:
        text += f"- {k}\n"

    text += """
- System handles errors
- Ensures scalability

⚠️ **Edge Cases**
- Invalid inputs
- Security breaches
- High traffic

💡 **Suggestions**
- Add monitoring
- Enable alerts
"""

    return text


# =========================
# CHAT DISPLAY
# =========================
st.markdown("### 💬 AI BA Assistant")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =========================
# INPUT BOX (FIXED ALWAYS SHOWS)
# =========================
user_input = st.chat_input("Describe your requirement...")

if user_input:

    # show user msg
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):

        result = generate_response(user_input)

        # if conversational
        if isinstance(result, str):
            st.markdown(result)
            st.session_state.messages.append({"role": "assistant", "content": result})

