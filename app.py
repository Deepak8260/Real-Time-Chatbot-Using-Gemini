import streamlit as st
import google.generativeai as genai



# Configure API key
genai.configure(api_key="AIzaSyDsAVc-Jpsf5yi-2fhoZR3YMLuTpEFEBzM")

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content

st.title('Realtime Chatbot App')
input = st.text_input('Enter what you want to search')
button = st.button('Response')

if button:
    response = model.generate_content(input)
    st.write(response.text)

