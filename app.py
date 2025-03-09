import streamlit as st
import google.generativeai as genai
from text_interaction import handle_text_interaction
from db import insert_data
import os
import json
from dotenv import load_dotenv

# Get API key from Streamlit Secrets
API_KEY = st.secrets["GENAI_API_KEY"]

# Configure API key
genai.configure(api_key=API_KEY)

# Define structured data in JSON format
creator_info = {
    "name": "Deepak Kumar Mohanty",
    "role": "Aspiring Data Scientist",
    "education": "BCA from Bhadrak Autonomous College, Odisha",
    "skills": ["Python", "Machine Learning", "Data Analysis", "Django", "Flask"],
    "linkedin": "https://www.linkedin.com/in/deepak-kumar-mohanty-09aa59230/",
    "personal_info": {
        "hobbies": ["Watching movies", "Exploring and learning new tech, especially in AI"],
        "weight": "92.5 kg",
        "height": "5 feet 8 inches",
        "family_members": 6,
        "address": "Odisha, India",
        "email": "kd.codegeek@gmail.com"
    }
}

# Convert JSON to string
SYSTEM_PROMPT = f"""
You are a chatbot created by Deepak Kumar Mohanty. Here is some information about your creator:

{json.dumps(creator_info, indent=2)}

If anyone asks about the creator, always mention Deepak Kumar Mohanty. If anyone asks for more details, refer them to his LinkedIn profile.
"""

# Load the model (without system_instruction)
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title('Realtime Chatbot App')

def handle_text_interaction(model):
    """Handles text-to-text chatbot interaction"""
    user_input = st.text_input('Enter your query:')
    button = st.button('Get Response')

    if button and user_input:
        # Append SYSTEM_PROMPT dynamically to ensure responses align with creator info
        full_prompt = SYSTEM_PROMPT + "\nUser Query: " + user_input
        
        response = model.generate_content(full_prompt)
        st.write(response.text)

        return {"user_input": user_input, "response": response.text}  # ✅ Return response

    return None  # ✅ Return None if no response

# Call text interaction function
response = handle_text_interaction(model)

if response:
    insert_data(response['user_input'], response['response'])
