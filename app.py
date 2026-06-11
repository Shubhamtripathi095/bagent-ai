import streamlit as st

# =====================
# PAGE CONFIG & SYSTEM SETUP
# =====================
st.set_page_config(
    page_title="BAGENT.AI - Copilot for Business Analysis", 
    layout="wide",
    page_icon="🚀"
)

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
# HELPER FUNCTIONS & MOCK BA ENGINE
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

def generate_local_ba_response(user_input, domain, output_format):
    """
    Generates structured BA artifacts locally without calling external APIs.
    """
    clean_input = user_input.replace(f"[Format requested: {output_format}] ", "")
    
    if "SWOT" in output_format:
        return f"""
### 📊 SWOT & Strategic Analysis
**Project Scope:** *{clean_input}*
**Target Domain:** {domain}

| **Strengths** (Internal) | **Weaknesses** (Internal) |
| :--- | :--- |
| • Modern technical framework stack.<br>• Automated processing capabilities. | • High initial setup complexity.<br>• Data privacy alignment risks. |

| **Opportunities** (External) | **Threats** (External) |
| :--- | :--- |
| • Rapidly growing demand in {domain}.<br>• Scalable cloud infrastructure potential. | • Evolving regulatory compliances.<br>• Intense market competition. |
        """
        
    elif "Functional" in output_format:
        return f"""
### 📋 Functional Specifications (FRD)
**Project Scope:** *{clean_input}*
**Target Domain:** {domain}

#### 1. Functional Requirements
* **FR-01 (Authentication):** The system MUST authenticate users safely before granting system workspace access.
* **FR-02 (Data Processing):** The core engine MUST log transactions related to *"{clean_input}"* with an audit trail timestamp.
* **FR-03 (Reporting):** Users MUST be able to export a summary dashboard of activities into a CSV format.

#### 2. Non-Functional Requirements
* **NFR-01 (Performance):** Queries must execute in under 2.0 seconds under peak load conditions.
* **NFR-02 (Security):** All data in transit within the {domain} environment must be encrypted using TLS 1.3.
        """
        
    else:  # Default to Agile User Stories & BRD
        return f"""
### 📝 Agile User Stories & BRD
**Project Scope:** *{clean_input}*
**Target Domain:** {domain}

#### **US-101: Core Workspace Setup**
* **As a** Registered User  
* **I want to** access the feature module for *"{clean_input}"* * **So that** I can manage my workspace workflow parameters effectively.

#### **📋 Acceptance Criteria (Given/When/Then)**
* **Scenario 1: Successful Validation**
  * **Given** the user is logged into a verified account within the **{domain}** platform,
  * **When** they navigate to the primary dashboard view,
  * **Then** the interface components for *"{clean_input}"* should render completely within 1.5 seconds.
        """

# =====================
# UI LAYOUT
# =====================
st.title("🚀 BAGENT.AI")
st.caption("Copilot for Business Analysis & Product Requirement Generation")
st.markdown("---")

# Sidebar Configuration Options
with st.sidebar:
    st.header("🎯 Agent Control Panel")
    output_format = st.selectbox(
        "Preferred Deliverable Format",
        ["Agile User Stories & BRD", "Functional Specifications (FRD)", "SWOT & Strategic Analysis"]
    )
    st.info("💡 **Note:** Running in local execution engine mode. No external API keys required.")

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
    
    # Track the format requested alongside input history
    modified_input = f"[Format requested: {output_format}] {user_input}"
    st.session_state.messages[-1]["content"] = modified_input

    # 3. Generate and Display Local Engine Response
    with st.chat_message("assistant"):
        with st.spinner(f"Compiling specifications for **{detected_domain}** domain..."):
            local_response = generate_local_ba_response(user_input, detected_domain, output_format)
            st.markdown(local_response)
            
    # Save response to session state
    st.session_state.messages.append({"role": "assistant", "content": local_response})
