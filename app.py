import streamlit as st
import google.generativeai as genai
from text_interaction import handle_text_interaction

# Configure API key
genai.configure(api_key="AIzaSyDsAVc-Jpsf5yi-2fhoZR3YMLuTpEFEBzM")

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title('Realtime Chatbot App')

# Call text interaction function directly
handle_text_interaction(model)
