import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure API key
genai.configure(api_key=api_key)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content

st.title('Realtime Chatbot App')
input = st.text_input('Enter what you want to search')
button = st.button('Response')

if button:
    response = model.generate_content(input)
    st.write(response.text)

