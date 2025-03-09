import streamlit as st
import google.generativeai as genai
from text_interaction import handle_text_interaction
from db import insert_data
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("GENAI_API_KEY")

# Configure API key
genai.configure(api_key=API_KEY)


# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title('Realtime Chatbot App')


# Call text interaction function directly
response = handle_text_interaction(model)

if response:
    #print("Storing in DB:", response)  # ✅ Debug print
    insert_data(response['user_input'], response['response'])
