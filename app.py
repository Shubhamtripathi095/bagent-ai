import streamlit as st
import time

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# =====================
# HEADER
# =====================
st.title("🚀 BAGENT.AI")
st.caption("AI Copilot for Business Analysis")
st.markdown("---")

# =====================
# STATE INIT (IMPORTANT)
# =====================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello — I’m your AI Business Analyst.\n\nDescribe a system and I will convert it into structured requirements."
        }
    ]

if "context" not in st.session_state:
    st.session_state.context = ""

# =====================
# DOMAIN DETECTION
# =====================
def detect_domain(text):
    t = text.lower()
    if "loan" in t or "bank" in t:
        return "Finance"
    if "hospital" in t or "patient" in t:
        return "Healthcare"
    if "checkout" in t or "cart" in t:
        return "E-commerce"
    return "General"

# =====================
# RESPONSE LOGIC (FIXED)
# =====================
def generate_response(user_input):
    t = user_input.lower()

    if t in ["hi", "hello"]:
        return "Hello. Please describe what system you want to build."

    if "wow" in t:
        return "Glad that helped. You can refine or expand your requirement."

    if len(user_input) < 8:
        return "Please provide more detail about your requirement."

    # store context
    st.session_state.context += " " + user_input

    domain = detect_domain(st.session_state.context)
    return domain, st.session_state.context

# =====================
# OUTPUT BUILDER
# =====================
def build_output(context, domain):
    return f"""
### Understanding
This is a **{domain} system** with defined flows and validations.

---

### User Story
As a user,  
I want to {context},  
So that I achieve the expected outcome.

---

### Acceptance Criteria
- Input validation  
- Security checks  
- Error handling  
- Data consistency  

---

### Edge Cases
- Invalid inputs  
- System failures  
- Security risks  

---

### Recommendation
Use modular architecture and scalable design.
"""

# =====================
# CHAT DISPLAY
# =====================
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# =====================
# INPUT
# =====================
user_input = st.chat_input("Describe your requirement...")

if user_input:

    # USER message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ASSISTANT RESPONSE
    response = generate_response(user_input)

    with st.chat_message("assistant"):

        # conversational
        if isinstance(response, str):
            st.markdown(response)
            st.session_state.messages.append({
                "role": "assistant",
