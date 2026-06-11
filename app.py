import streamlit as st

st.set_page_config(page_title="BAGENT.AI", page_icon="🚀", layout="wide")

st.title("🚀 BAGENT.AI")
st.caption("Autonomous Business Analyst Copilot")

requirement = st.text_area(
    "Enter Business Requirement",
    height=150,
    placeholder="Example: Build a Loan Origination System for Auto Finance"
)

def detect_domain(text):
    text = text.lower()
    if any(x in text for x in ["loan","finance","bank","credit"]):
        return "BFSI"
    if any(x in text for x in ["hospital","patient"]):
        return "Healthcare"
    if any(x in text for x in ["cart","checkout","order"]):
        return "E-Commerce"
    return "Generic"

if st.button("Generate BA Artifacts") and requirement:

    domain = detect_domain(requirement)

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "BRD","FRD","SRS","Epics","User Stories",
        "Acceptance Criteria","Gherkin","Test Cases","Process Flow"
    ])

    with tab1:
        st.markdown(f"""
# Business Requirement Document

## Domain
{domain}

## Business Objective
{requirement}

## Scope
Deliver the requested business capability.

## Stakeholders
- Customer
- Business User
- Operations Team
- Admin
""")

    with tab2:
        st.markdown("""
# Functional Requirement Document

FR-001 User can submit request

FR-002 System validates request

FR-003 System stores data

FR-004 System provides confirmation
""")

    with tab3:
        st.markdown("""
# Software Requirement Specification

## Functional Requirements
System shall process requests.

## Non Functional Requirements
- Availability: 99.9%
- Response Time: <3 sec
- Secure access required
""")

    with tab4:
        st.markdown("""
# Epics

EPIC-001 Customer Onboarding

EPIC-002 Request Processing

EPIC-003 Reporting
""")

    with tab5:
        st.markdown(f"""
# User Story

As a Business User

I want {requirement}

So that business operations become efficient.
""")

    with tab6:
        st.markdown("""
# Acceptance Criteria

- User can submit request
- Mandatory validation works
- Data saved successfully
- Confirmation displayed
""")

    with tab7:
        st.code("""Feature: Request Processing

Scenario: Successful Request

Given valid details entered
When request is submitted
Then system processes request
""")

    with tab8:
        st.markdown("""
# Test Cases

TC-001 Verify successful submission

TC-002 Verify mandatory validations

TC-003 Verify error handling
""")

    with tab9:
        st.markdown("""
# Process Flow

As-Is:
Manual Processing

To-Be:
Digital Submission -> Validation -> Processing -> Confirmation
""")
