import streamlit as st
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="BAGENT.AI",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e293b);
}

.block-container{
max-width:1200px;
padding-top:2rem;
}

h1,h2,h3,h4,p,label{
color:white !important;
}

.card{
background:rgba(255,255,255,0.05);
backdrop-filter: blur(10px);
padding:18px;
border-radius:14px;
border:1px solid rgba(255,255,255,0.1);
text-align:center;
font-weight:600;
color:white;
}

.stButton > button{
width:100%;
background:linear-gradient(90deg,#6366f1,#06b6d4);
color:white;
border:none;
border-radius:10px;
padding:10px;
font-weight:bold;
}

div[data-baseweb="input"] input{
background:#0f172a !important;
color:white !important;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀 BAGENT.AI")
st.caption("Autonomous Multi-Agent Business Analyst")

# --------------------------------------------------
# CAPABILITIES
# --------------------------------------------------

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

# --------------------------------------------------
# DOMAIN DETECTOR
# --------------------------------------------------

def detect_domain(text):

    text = text.lower()

    if any(x in text for x in ["loan","bank","finance","credit"]):
        return "BFSI"

    elif any(x in text for x in ["hospital","patient","doctor"]):
        return "Healthcare"

    elif any(x in text for x in ["cart","checkout","product","order"]):
        return "E-Commerce"

    elif any(x in text for x in ["employee","payroll","hr"]):
        return "HR"

    return "Generic"

# --------------------------------------------------
# GENERATORS
# --------------------------------------------------

def generate_user_story(req):

    return f"""
### User Story

**As a** Business User

**I want** {req}

**So that** business operations become efficient and automated.
"""

def generate_acceptance():

    return """
### Acceptance Criteria

✅ User can submit request

✅ System validates mandatory fields

✅ System stores data successfully

✅ User receives confirmation

✅ Errors are handled gracefully
"""

def generate_gherkin():

    return """
### Gherkin Scenario

```gherkin
Feature: Requirement Processing

Scenario: Successful submission

Given user enters valid information

When user submits request

Then system validates data

And stores information

And displays confirmation message
