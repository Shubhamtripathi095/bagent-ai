st.markdown("""
<style>

/*.block-container {/* Main container fix */
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Headings brighter */
h1, h2, h3, h4 {
    color: #e2e8f0;
}

/* Cards */
.card {
    background: #1e293b;
    padding: 16px;
    border-radius: 10px;
    border: 1px solid rgba(56,189,248,0.4);
}

/* Fix faded text */
p, span, label {
    color: #e2e8f0 !important;
}

/* Input box */
input {
    background-color: #0f172a !important;
    color: white !important;
}

/* Fix button */
button {
    background: linear-gradient(90deg, #6366f1, #06b6d4);
    color: white;
    border-radius: 8px;
}

/* Remove weird extra spacing */
section.main > div {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)
