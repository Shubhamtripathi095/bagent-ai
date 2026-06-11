import streamlit as st
import os
from openai import OpenAI

# =====================
# PAGE CONFIG & SYSTEM SETUP
# =====================
st.set_page_config(
    page_title="BAGENT.AI - Copilot for Business Analysis", 
    layout="wide",
    page_icon="🚀"
)

# Initialize OpenAI Client (Make sure OPENAI_API_KEY is set in your environment variables or Streamlit secrets)
# If testing locally, you can use: os.environ["OPENAI_API_KEY"] = "your-key"
ai_client = OpenAI()

# =====================
# SESSION STATE INITIALIZATION
# =====================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hello! I’m your AI Business Analyst Copilot. 🚀\n\nDescribe the system, feature, or business problem you are working on, and I will help you structure it into professional BA artifacts."
        }
    ]

# =====================
# HELPER FUNCTIONS
# =====================
def detect_domain(text):
    """Simple heuristic rule engine to flag domain focus areas."""
    text = text.lower()
    if any(w in text for w in ["loan", "bank", "payment", "checkout", "stripe", "ledger"]):
        return "FinTech / Finance"
    elif any(w in text for w in ["patient", "clinic", "ehr", "doctor", "medical"]):
        return "Healthcare"
    elif any(w in text for w in ["cart", "shop", "product", "inventory", "shipping"]):
        return "E-Commerce"
    return "General Software / Business"

def get_ai_ba_response(messages, domain):
    """Calls OpenAI API with a customized system prompt tailoring output to BA standards."""
    
    system_prompt = f"""
    You are an expert Senior Business Analyst and Product Manager. Your job is to help users break down system descriptions into structured, professional BA artifacts.
    Current Detected Industry Domain: {domain}
    
    When responding:
    1. Be highly structured. Use Markdown headings, tables, and bullet points.
    2. Depending on what the user asks, provide standard BA deliverables:
       - User Stories (Format: As a... I want to... So that...) with explicit Acceptance Criteria (Given/When/Then).
       - Functional & Non-Functional Requirements.
       - Process flows or brief SWOT analysis if applicable.
    3. Keep your tone professional, consultative, and sharp.
    """
    
    # Prepend system prompt to the conversation history
    api_messages = [{"role": "system", "content": system_prompt}] + [
        {"role": m["role"], "content": m["content"]} for m in messages
    ]
    
    try:
        response = ai_client.chat.completions.create(
            model="gpt-4o-mini", # High speed, cost-effective model for structuring text
            messages=api_messages,
            temperature=0.2 # Lower temperature for analytical, less chaotic responses
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error generating analysis: {str(e)}"

# =====================
# UI LAYOUT
# =====================
st.title("🚀 BAGENT.AI")
st.caption("AI Copilot for Business Analysis & Product Requirement Generation")
st.markdown("---")

# Sidebar Configuration Options
with st.sidebar:
    st.header("🎯 Agent Control Panel")
    output_format = st.selectbox(
        "Preferred Deliverable Format",
        ["Agile User Stories & BRD", "Functional Specifications (FRD)", "SWOT & Strategic Analysis"]
    )
    st.info("💡 **Tip:** Mention specific user roles (e.g., 'Admin', 'Customer') in your text to get cleaner acceptance criteria!")

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input Interface
if user_input := st.chat_input("Describe the system or feature you want to build..."):
    
    # 1. Display User Message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
        
    # 2. Run Domain Detection Strategy
    detected_domain = detect_domain(user_input)
    
    # Add context tracking to user's input if format preferences change
    modified_input = f"[Format requested: {output_format}] {user_input}"
    st.session_state.messages[-1]["content"] = modified_input

    # 3. Generate and Stream/Display Bot Response
    with st.chat_message("assistant"):
        with st.spinner(f"Analyzing specifications for **{detected_domain}** domain..."):
            ai_response = get_ai_ba_response(st.session_state.messages, detected_domain)
            st.markdown(ai_response)
            
    # Save assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
