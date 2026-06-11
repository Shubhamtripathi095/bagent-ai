import streamlit as st
from services.gemini_service import generate_ba_package

st.set_page_config(
    page_title="BAGENT.AI",
    page_icon="🚀",
    layout="wide"
)

# -------------------------------
# CSS
# -------------------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(
135deg,
#0f172a,
#1e293b,
#111827
);
}

.main-title{
font-size:48px;
font-weight:700;
color:white;
}

.agent-card{
background:rgba(255,255,255,0.05);
padding:20px;
border-radius:15px;
border:1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------

st.markdown(
"""
<div class='main-title'>
🚀 BAGENT.AI
</div>
""",
unsafe_allow_html=True
)

st.caption(
"Autonomous Business Analyst Copilot"
)

# -------------------------------
# DOMAIN
# -------------------------------

domain = st.selectbox(
    "Select Domain",
    [
        "BFSI",
        "Auto Finance",
        "Retail Banking",
        "Wealth Management",
        "Healthcare",
        "E-Commerce"
    ]
)

# -------------------------------
# REQUIREMENT
# -------------------------------

requirement = st.text_area(
    "Business Requirement",
    height=200,
    placeholder="""
Example:

Build a Loan Origination System
for Auto Finance supporting:

- Customer Onboarding
- KYC Verification
- Credit Assessment
- Loan Approval
- Loan Disbursement
"""
)

# -------------------------------
# GENERATE
# -------------------------------

if st.button("🚀 Generate BA Package"):

    if not requirement.strip():

        st.warning(
            "Please enter requirement."
        )

    else:

        with st.spinner(
            "🤖 Discovery Agent analysing requirement..."
        ):

            response = generate_ba_package(
                f"""
Domain:
{domain}

Requirement:
{requirement}
"""
            )

        st.success(
            "BA Package Generated"
        )

        tabs = st.tabs([
            "📘 Output",
            "📥 Download"
        ])

        with tabs[0]:

            st.markdown(response)

        with tabs[1]:

            st.download_button(
                "Download BA Package",
                response,
                file_name="BA_Package.md"
            )
