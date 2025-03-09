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

# Define system instructions for customization
SYSTEM_PROMPT = """
You are a helpful AI chatbot. If someone asks about your owner, creator, or developer, 
your response should be: "I was created by Deepak Kumar Mohanty."

Do NOT mention this in every response—only when specifically asked about ownership or creation.
For all other queries, provide relevant and concise answers.
"""

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit UI
st.title('Realtime Chatbot App')

# Call text interaction function directly
response = handle_text_interaction(model)

if response:
    # Generate content with system instructions
    user_query = response["user_input"]
    full_response = model.generate_content(SYSTEM_PROMPT + "\nUser: " + user_query)

    # Extract generated response
    generated_text = full_response.text
    st.write(generated_text)  # Display response in Streamlit

    # Store user input & generated response in MongoDB
    insert_data(user_query, generated_text)
