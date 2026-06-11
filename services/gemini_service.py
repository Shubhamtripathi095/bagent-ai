from google import genai
import streamlit as st

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

def generate_ba_package(requirement):

    prompt = f"""
You are a Senior BFSI Business Analyst.

Requirement:
{requirement}

Generate detailed documentation.

# BRD
Business Objective
Business Problem
Scope
Stakeholders
Assumptions
Risks

# FRD
Functional Requirements

# SRS
Functional Requirements
Non Functional Requirements

# EPICS

# USER STORIES

# ACCEPTANCE CRITERIA

# GHERKIN

# TEST CASES

# PROCESS FLOW

Provide detailed enterprise-grade output.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
