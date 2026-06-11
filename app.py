import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI ELITE", layout="wide")

# =========================
# HEADER
# =========================
st.title("🚀 BAGENT.AI ELITE")
st.caption("Conversational Multi-Agent AI Business Analyst (RAG + Context Engine)")

st.markdown("---")

# =========================
# SESSION STATE
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = ""

# =========================
# WELCOME MESSAGE
# =========================
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": """
👋 **Welcome to BAGENT.AI ELITE**

I can help you:
- Convert ideas into user stories  
- Generate acceptance criteria  
- Identify edge cases  
- Provide AI-driven insights  

### 🚀 Try:
- Build a loan system with fraud detection  
- Create hospital patient system  
- Design e-commerce checkout  
"""
    })

# =========================
# DOMAIN DETECTION
# =========================
def detect_domain(text):
    text = text.lower()
    if any(x in text for x in ["loan","bank","finance"]):
        return "Finance"
    if any(x in text for x in ["hospital","patient","health"]):
        return "Healthcare"
    if any(x in text for x in ["checkout","cart","order"]):
        return "E-commerce"
    if any(x in text for x in ["employee","hr","payroll"]):
        return "HR"
    return "Generic"

# =========================
# KNOWLEDGE BASE (RAG STYLE)
# =========================
knowledge_base = {
    "Finance": ["KYC compliance", "Fraud detection", "Secure transactions"],
    "Healthcare": ["HIPAA compliance", "Patient data protection"],
    "E-commerce": ["Cart management", "Payment gateway", "Refund workflows"],
    "HR": ["Payroll validation", "Employee data security"],
    "Generic": ["Validation rules", "Security checks"]
}

# =========================
# AI LOGIC
# =========================
def generate_response(user_input):

    text = user_input.lower()

    # ✅ conversational mode
    if text in ["hi","hello","hey"]:
        return "👋 Hi! Tell me what system you'd like to build."

    if "wow" in text:
        return "😄 Glad you liked it! Want to enhance the requirement further?"

    if "thank" in text:
        return "🙏 You're welcome! Let me know what you'd like to explore next."

    if len(user_input.split()) < 3:
        return "🤖 Could you please provide more detailed system requirements?"

    # ✅ CONTEXT MEMORY
    st.session_state.context += " " + user_input
    combined = st.session_state.context

    domain = detect_domain(combined)
    knowledge = knowledge_base[domain]

    steps = [
        "🧠 Discovery Agent → Understanding requirement...",
        "🌐 Knowledge Agent → Enriching context...",
        "🛡️ Audit Agent → Validating constraints...",
        "✍️ Writer Agent → Generating output..."
    ]

    return steps, combined, domain, knowledge


# =========================
# OUTPUT BUILDER
# =========================
def build_output(combined, domain, knowledge):

    explanation = f"""
🧠 **Understanding**

