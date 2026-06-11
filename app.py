import streamlit as st
import time

st.set_page_config(page_title="BAGENT.AI", layout="wide")

st.title("🤖 BAGENT.AI")
st.caption("Autonomous Multi-Agent BA Orchestrator")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "idle"

col1, col2 = st.columns([1.2, 1])

with col1:
    st.subheader("🧠 Discovery Workspace")

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

    user_input = st.chat_input("Describe your feature requirement...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        if st.session_state.stage == "idle":
            response = "🔍 Understanding requirements..."
            st.session_state.stage = "discovery"
        elif st.session_state.stage == "discovery":
            response = "🛡️ Running compliance checks..."
            st.session_state.stage = "audit"
        elif st.session_state.stage == "audit":
            response = "✅ Generating Jira-ready user story..."
            st.session_state.stage = "output"
        else:
            response = "🔄 Reset to start again"

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

with col2:
    st.subheader("⚙️ Agent Control Panel")

    st.markdown("### Agents")

    st.write("Lead BA Agent:", "✅" if st.session_state.stage != "idle" else "⏳")
    st.write("Audit Agent:", "✅" if st.session_state.stage in ["audit", "output"] else "⏳")
    st.write("Writer Agent:", "✅" if st.session_state.stage == "output" else "⏳")

    if st.session_state.stage == "idle":
        st.info("Waiting for input")

    if st.session_state.stage == "audit":
        st.write("Checking schema...")
        time.sleep(0.5)
        st.write("Validating compliance...")
        time.sleep(0.5)
        st.success("All checks passed")

    if st.session_state.stage == "output":
        st.success("User Story Generated ✅")

        st.code("""
As a user,
I want to complete checkout,
So that I can purchase items.

Acceptance Criteria:
- Payment should be secure
- Support card + PayPal
""")

    if st.button("Reset"):
        st.session_state.clear()
        st.rerun()
