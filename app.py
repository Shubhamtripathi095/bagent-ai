import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI", layout="wide")

# =========================
# HEADER
# =========================
st.title("🚀 BAGENT.AI")
st.caption("AI Business Analyst | RAG + Multi-Agent Simulation")

# =========================
# SESSION STATE (CHAT)
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

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
# KNOWLEDGE BASE (RAG STYLE)
# =========================
domain_knowledge = {
    "Finance": ["KYC compliance", "Fraud detection", "Transaction security"],
    "Healthcare": ["HIPAA compliance", "Data privacy", "Audit logs"],
    "E-commerce": ["Payment gateway", "Cart flow", "Refund system"],
    "HR": ["Payroll validation", "Employee records", "Access management"],
    "Generic": ["Validation rules", "Security checks"]
}

# =========================
# AI GENERATION FUNCTION
# =========================
def generate_ai_response(user_input):
    domain = detect_domain(user_input)
    knowledge = domain_knowledge[domain]

    response = f"""
🧠 **Understanding Your Requirement**

This looks like a **{domain} domain system**.  
Let me break this down and structure it professionally.

---

📌 **User Story**

As a user,  
I want to {user_input},  
So that I can achieve the intended outcome.

---

✅ **Acceptance Criteria**
"""
    for k in knowledge:
        response += f"- {k}\n"

    response += """
- System handles errors  
- Ensures data integrity  

---

⚠️ **Edge Cases**
- Invalid input handling  
- System downtime scenarios  
- Security breaches  

---

💡 **AI Suggestions**
- Add monitoring dashboards  
- Include logging & alerts  
- Design scalable architecture  

---

✨ **Summary**
This system should be designed with strong validation, compliance, and modular architecture.
"""

    return response


# =========================
# CHAT UI
# =========================
st.markdown("### 💬 AI BA Assistant")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# INPUT BOX
user_input = st.chat_input("Describe your requirement...")

if user_input:

    # USER message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # AI response (with streaming feel)
    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_text = ""

        steps = [
            "🔍 Analyzing requirement...",
            "📚 Fetching knowledge...",
            "⚙️ Applying logic...",
            "✍️ Generating structured output..."
        ]

        for step in steps:
            placeholder.markdown(step)
            time.sleep(0.5)

        final_response = generate_ai_response(user_input)

        for word in final_response.split():
            full_text += word + " "
            placeholder.markdown(full_text)
            time.sleep(0.01)

    st.session_state.messages.append({"role": "assistant", "content": final_response})


# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.header("🧠 Knowledge Engine")

    st.markdown("""
✅ Domain Detection  
✅ Knowledge Retrieval  
✅ Context Enrichment  
✅ Structured Output  

🚀 Future Upgrade:
- Vector DB  
- Real RAG  
- Enterprise data  
""")
