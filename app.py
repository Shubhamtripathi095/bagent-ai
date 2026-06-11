import streamlit as st
import time

# ==========================
# CONFIG
# ==========================
st.set_page_config(page_title="BAGENT.AI", layout="wide")

# ==========================
# STYLE
# ==========================
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Text */
h1, h2, h3, h4, p, label {
    color: #e2e8f0 !important;
}

/* Cards */
.card {
    background: linear-gradient(145deg, #1e293b, #0f172a);
    padding: 18px;
    border-radius: 12px;
    border: 1px solid rgba(56,189,248,0.5);
    box-shadow: 0 0 15px rgba(56,189,248,0.2);
}

/* Input */
input {
    background-color: #0f172a !important;
    color: white !important;
    border: 1px solid rgba(56,189,248,0.5) !important;
    box-shadow: 0 0 8px rgba(56,189,248,0.2);
}

/* Buttons */
button {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
