import streamlit as st
from services.gemini_service import generate_ba_package

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="BAGENT.AI",
    page_icon="🚀",
    layout="wide"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#0f172a,
#1e293b,
#111827
);
}

.main-title{
font-size:52px;
font-weight:800;
color:white;
}

.main-subtitle{
color:#cbd5e1;
font-size:18px;
margin-bottom:20px;
}

h1,h2,h3,h4,h5,h6{
color:white !important;
}

p,li{
color:#e5e7eb !important;
}

div[data-testid="stMarkdownContainer"]{
color:#f8fafc !important;
}

.agent-card{
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:16px;
border:1px solid rgba(255,255,255,0.1);
text-align:center;
}

.stButton button{
background:linear-gradient(
90deg,
#3b82f6,
#06b6d4
);
color:white;
border:none;
border-radius:10px;
font-weight:bold;
padding:10px 20px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================

st.markdown(
"""
<div class='main-title'>
🚀 BAGENT.AI
</div>

<div class='main-subtitle'>
Autonomous Multi-Agent Business Analyst Copilot
</div>
""",
unsafe_allow_html=True
)

# ==================================================
# CAPABILITY CARDS
# ==================================================

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.info("""
📘 Documentation

✔ BRD
✔ FRD
✔ SRS
""")

with col2:
    st.info("""
🚀 Agile

✔ Epics
✔ User Stories
✔ Acceptance Criteria
""")

with col3:
    st.info("""
🧪 QA

✔ Gherkin
✔ Test Cases
✔ UAT Scenarios
""")

with col4:
    st.info("""
🏦 BFSI

✔ LOS
✔ LMS
✔ Lending
""")

st.divider()

# ==================================================
# DOMAIN
# ==================================================

domain = st.selectbox(
    "🏦 Select Domain",
    [
        "BFSI",
        "Auto Finance",
        "Retail Banking",
        "Wealth Management",
        "Healthcare",
        "E-Commerce"
    ]
)

# ==================================================
# REQUIREMENT
# ==================================================

requirement = st.text_area(
    "📝 Business Requirement",
    height=220,
    placeholder="""
Example:

Build a Loan Origination System for Auto Finance

Capabilities:

- Customer Onboarding
- KYC Verification
- Credit Assessment
- Loan Approval
- Loan Disbursement
- Dealer Management
- Reporting Dashboard
"""
)

# ==================================================
# GENERATE
# ==================================================

if st.button("🚀 Generate BA Package"):

    if not requirement.strip():

        st.warning(
            "Please enter a business requirement."
        )

    else:

        with st.status(
            "Running Multi-Agent BA Workflow...",
            expanded=True
        ) as status:

            st.write("🧠 Discovery Agent")
            st.write("📘 BRD Agent")
            st.write("📗 FRD Agent")
            st.write("📕 SRS Agent")
            st.write("🚀 Agile Agent")
            st.write("🧪 QA Agent")

            response = generate_ba_package(
                f"""
Domain:
{domain}

Requirement:
{requirement}
"""
            )

            status.update(
                label="All Agents Completed",
                state="complete"
            )

        st.success("✅ BA Package Generated Successfully")

        tab1, tab2 = st.tabs(
            [
                "📘 Generated Package",
                "📥 Download"
            ]
        )

        with tab1:

            st.markdown(response)

        with tab2:

            st.download_button(
                label="📥 Download BA Package",
                data=response,
                file_name="BAGENT_AI_Package.md",
                mime="text/markdown"
            )

st.divider()

st.caption(
    "Powered by Gemini + BAGENT.AI | Autonomous Business Analyst Platform"
)
