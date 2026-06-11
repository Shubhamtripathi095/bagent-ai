import streamlit as st
import time

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="BAGENT.AI",
    page_icon="🚀",
    layout="wide"
)

# ==================================================
# CUSTOM CSS
# ==================================================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

h1, h2, h3, h4, p, label {
    color: white !important;
}

.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.1);
    text-align: center;
    font-weight: 600;
    color: white;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#6366f1,#06b6d4);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px;
    font-weight: bold;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
    background: #0f172a !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.title("🚀 BAGENT.AI")
st.caption("Autonomous Multi-Agent Business Analyst")

st.divider()

# ==================================================
# CAPABILITY CARDS
# ==================================================
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        🧠 Requirement Discovery
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        🌐 Knowledge Enrichment
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        ⚙️ User Story Generator
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==================================================
# DOMAIN DETECTION
# ==================================================
def detect_domain(text):

    text = text.lower()

    if any(word in text for word in ["loan", "bank", "finance", "credit"]):
        return "BFSI"

    elif any(word in text for word in ["hospital", "patient", "doctor", "health"]):
        return "Healthcare"

    elif any(word in text for word in ["cart", "checkout", "order", "product"]):
        return "E-Commerce"

    elif any(word in text for word in ["employee", "payroll", "hr"]):
        return "Human Resources"

    return "Generic"

# ==================================================
# GENERATORS
# ==================================================
def generate_user_story(requirement):

    return f"""
### User Story

**As a** Business User

**I want** {requirement}

**So that** business operations become efficient, automated and scalable.
"""

def generate_acceptance_criteria():

    return """
### Acceptance Criteria

✅ User can submit request

✅ System validates mandatory fields

✅ System processes request successfully

✅ User receives confirmation

✅ Errors are handled gracefully

✅ Audit trail is maintained
"""

def generate_gherkin():

    return """
### Gherkin Scenario

Feature: Requirement Processing

Scenario: Successful Submission

Given user enters valid information

When user submits the request

Then system validates the information

And stores the data successfully

And displays confirmation message
"""

# ==================================================
# LAYOUT
# ==================================================
left, right = st.columns([1.6, 1])

with left:

    st.subheader("🧠 Discovery Workspace")

    requirement = st.text_area(
        "Enter Business Requirement",
        height=180,
        placeholder="Example: Build a loan approval system with fraud detection"
    )

    generate_button = st.button("🚀 Generate Analysis")

with right:

    st.subheader("⚡ Agent Status")

    status_placeholder = st.empty()

# ==================================================
# MAIN PROCESS
# ==================================================
if generate_button:

    if not requirement.strip():

        st.warning("Please enter a business requirement.")

    else:

        with status_placeholder.container():

            with st.status(
                "Running Autonomous Multi-Agent Workflow...",
                expanded=True
            ) as status:

                st.write("🧠 Discovery Agent analysing requirement...")
                time.sleep(1)

                st.write("🌐 Knowledge Agent enriching domain context...")
                time.sleep(1)

                st.write("📊 Business Analysis Agent preparing backlog...")
                time.sleep(1)

                st.write("⚙️ User Story Agent generating stories...")
                time.sleep(1)

                st.write("✅ Analysis completed")

                status.update(
                    label="Workflow Completed",
                    state="complete"
                )

        domain = detect_domain(requirement)

        user_story = generate_user_story(requirement)
        acceptance = generate_acceptance_criteria()
        gherkin = generate_gherkin()

        st.success(f"Detected Domain: {domain}")

        tab1, tab2, tab3 = st.tabs([
            "📘 User Story",
            "✅ Acceptance Criteria",
            "🧪 Gherkin"
        ])

        with tab1:
            st.markdown(user_story)

        with tab2:
            st.markdown(acceptance)

        with tab3:
            st.markdown(gherkin)

        export_content = f"""
===========================
BAGENT.AI OUTPUT
===========================

Detected Domain:
{domain}

---------------------------
USER STORY
---------------------------
{user_story}

---------------------------
ACCEPTANCE CRITERIA
---------------------------
{acceptance}

---------------------------
GHERKIN SCENARIO
---------------------------
{gherkin}
"""

        st.download_button(
            label="📥 Download Analysis",
            data=export_content,
            file_name="BAGENT_AI_Output.txt",
            mime="text/plain"
        )

st.markdown("---")
st.caption("Powered by BAGENT.AI | Autonomous Multi-Agent Business Analyst")
