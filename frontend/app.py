# frontend/app.py
import streamlit as st
import requests
from ui_components import styled_button, custom_text_input # Import modular components

# Backend API URL (ensure this matches your backend's running port)
BACKEND_URL = "http://localhost:8000/analyze_topic/"

st.set_page_config(page_title="Research Paper Analyzer", layout="centered")
 
st.title("🔬 Topic Analyzer")
st.markdown("Enter a topic below and get a quick analysis from an AI.")

# User input for the topic
topic_input = custom_text_input(
    "Enter Topic:",
    placeholder="e.g., 'The impact of quantum computing on cryptography'",
    key="topic_input"
)

# Button to trigger analysis
if styled_button("Analyze Topic", key="analyze_button"):
    if topic_input:
        with st.spinner("Analyzing your topic..."):
            try:
                # Send request to backend
                response = requests.post(BACKEND_URL, json={"prompt": topic_input})
                response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
                result = response.json()
                st.subheader("Analysis Result:")
                st.write(result.get("response", "No response from AI."))
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the backend. Please ensure the backend server is running at http://localhost:8000.")
            except requests.exceptions.HTTPError as e:
                st.error(f"Backend error: {e.response.status_code} - {e.response.text}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter a research topic to analyze.")

st.markdown("---")
# st.info("Powered by Streamlit, FastAPI, and Groq LLM.")