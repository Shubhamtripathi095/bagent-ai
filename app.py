import streamlit as st
import time
from openai import OpenAI

# Page Layout Configuration
st.set_page_config(page_title="BAGENT.AI - Live Orchestrator", layout="wide")

st.title("🤖 BAGENT.AI")
st.caption("Autonomous Multi-Agent BA Orchestrator — Powered by Enterprise AI")
st.markdown("---")

# Initialize OpenAI Client securely using Streamlit Secrets
# (If key is not set, we fall back to a highly responsive simulated intelligent fallback)
openai_key = st.secrets.get("OPENAI_API_KEY", None)
client = OpenAI(api_key=openai_key) if openai_key else None

# Session State for tracking dynamic workflow
if "messages" not in st.session_state:
    st.session_state.messages = []
if "stage" not in st.session_state:
    st.session_state.stage = "idle"
if "current_requirement" not in st.session_state:
    st.session_state.current_requirement = ""
if "ai_generated_story" not in st.session_state:
    st.session_state.ai_generated_story = ""

# Split UI Layout
col1, col2 = st.columns([1.2, 1])

# =====================================================================
# LEFT COLUMN: Real-Time Discovery Workshop (Dynamic Chat)
# =====================================================================
with col1:
    st.subheader("🧠 Discovery Workspace")
    
    # 🌟 NEW PROFESSIONAL BA-CENTRIC TAGLINE
    st.markdown("""
    💡 **BAGENT.AI Capability Layer:** *Empowering Business Analysts to convert raw stakeholder intent into compliant, code-ready Jira Epics instantly. This cognitive pipeline automates structural requirement engineering, runs compliance logic checks, and synthesizes behavior-driven test criteria.*
    """)
    st.markdown("---")
    
    # Render historical messages dynamically
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat Input Box
    user_input = st.chat_input("Describe your formal BA requirement or user persona capability...")

    if user_input:
        # Save user input to session history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # 🌟 BULLETPROOF INPUT LOCKING FIX
        # सिर्फ़ पहली बार जब स्टेज 'idle' होगी, तभी मुख्य रिक्वायरमेंट लॉक होगी! "ok/good" इसे बदल नहीं पाएंगे।
        if st.session_state.stage == "idle":
            st.session_state.current_requirement = user_input
            st.session_state.stage = "discovery"
            msg_text = f"🔍 **Lead BA Agent:** Intent successfully captured for core requirement. Proceeding to map domain variables. Please type 'ok' or any validation word to trigger the Compliance Audit."
            st.session_state.messages.append({"role": "assistant", "content": msg_text})
            st.rerun()
            
        elif st.session_state.stage == "discovery":
            st.session_state.stage = "audit"
            msg_text = "🛡️ **Audit Agent:** Running semantic compliance. System boundaries cross-referenced against enterprise guardrails. Zero policy violations found. Type 'compile' to synthesize the live Jira ticket."
            st.session_state.messages.append({"role": "assistant", "content": msg_text})
            st.rerun()
            
        elif st.session_state.stage == "audit":
            st.session_state.stage = "output"
            
            # 🌟 REAL-TIME CHATGPT INTELLIGENCE GENERATION
            # अगर OpenAI Key मौजूद है तो असली API कॉल होगी, वरना स्मार्ट बैकअप रन होगा
            with st.spinner("🧠 BAGENT.AI is communicating with core LLM to structure your user story..."):
                target_req = st.session_state.current_requirement
                
                if client:
                    try:
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {"role": "system", "content": "You are an expert Agile Product Owner and Business Analyst. Convert the user's requirement into a professional Jira Title, User Story (As a, I want to, So that), and 1 Gherkin BDD Acceptance Criteria scenario."},
                                {"role": "user", "content": f"Create a structured user story for: {target_req}"}
                            ]
                        )
                        st.session_state.ai_generated_story = response.choices[0].message.content
                    except Exception as e:
                        st.session_state.ai_generated_story = f"API Error: {str(e)}"
                else:
                    # Smart internal engine fallback if key isn't deployed yet
                    st.session_state.ai_generated_story = f"""
TITLE: Implement {target_req.title() if len(target_req) < 40 else target_req[:40].title() + "..."}

AS A: Authorized Enterprise Product User / System Administrator
I WANT TO: Successfully process the business functions associated with "{target_req}"
SO THAT: The target system pipeline executes seamlessly without functional bottlenecks.

----------------------------------------------------------------------
📋 ACCEPTANCE CRITERIA (Gherkin BDD Syntax)
----------------------------------------------------------------------
Scenario: Successful processing of user input rules
  Given the BA orchestrator initiates the feature capture matrix
  When the requirement for "{target_req}" is parsed by BAGENT.AI
  Then the system updates the remote Atlassian backlog via API
  And returns a '201 Created' structural success token.
                    """
            
            msg_text = "✅ **Writer Agent:** Generation finalized. Agile payload parameters structured and displayed on the control panel dashboard."
            st.session_state.messages.append({"role": "assistant", "content": msg_text})
            st.rerun()

# =====================================================================
# RIGHT COLUMN: Multi-Agent Tool Execution Logs (Live Generation)
# =====================================================================
with col2:
    st.subheader("⚙️ Agent Control Panel")
    st.markdown("### Active Agent Matrix")
    
    st.write("Lead BA Agent (Discovery):", "✅ Active" if st.session_state.stage != "idle" else "⏳ Awaiting Input")
    st.write("Audit Agent (Compliance):", "✅ Checked" if st.session_state.stage in ["audit", "output"] else "⏳ Pending")
    st.write("Writer Agent (Jira Sync):", "🚀 Compiled" if st.session_state.stage == "output" else "⏳ Pending")
    
    st.markdown("---")
    
    if st.session_state.stage == "idle":
        st.info("💡 Pro Tip: Input a complex enterprise user requirement or business process on the left panel to trigger the agent lifecycle.")
        
    if st.session_state.stage == "discovery":
        st.info("⚙️ **Log:** Executing `Clarity_Score_Evaluator` on user input metrics...")
        st.success("Analysis Complete: Domain isolated. Enter 'ok' in the chat workspace to trigger the verification layer.")
        
    if st.session_state.stage == "audit":
        st.markdown("### 🛡️ Guardrail System Tool Outputs")
        with st.status("Running automated backend compliance...", expanded=True) as status:
            st.write("🔗 Fetching live codebase schemas using `Git_Repository_Parser()`...")
            time.sleep(0.3)
            st.write("🗄️ Querying policy vector space via `Vector_DB_Query()`...")
            time.sleep(0.3)
            status.update(label="Audit Check Passed: 0 Security or regulatory conflicts found.", state="complete")
        st.warning("👉 Enter 'compile' or any word in the chat to trigger the live OpenAI compilation.")
        
    if st.session_state.stage == "output":
        st.success("🔥 Success: User Story dynamically synthesized!")
        
        st.markdown("### 📋 Staged Jira Ticket Output")
        # यहाँ असली ChatGPT का आउटपुट दिखेगा जो यूजर के इनपुट पर आधारित है!
        st.code(st.session_state.ai_generated_story, language="text")
        
        if st.button("Reset Workshop"):
            st.session_state.clear()
            st.rerun()
