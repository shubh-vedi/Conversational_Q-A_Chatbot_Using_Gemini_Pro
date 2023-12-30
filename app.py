

# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai



# # Set background image
# st.markdown(
#     """<style>
#         body {
#             background-image: url('https://static.vecteezy.com/system/resources/previews/020/436/120/non_2x/chatbot-ai-artificial-intelligence-technology-hitech-concept-chatbot-application-smart-bot-open-ai-line-technology-abstract-design-for-chatting-web-banner-background-transformation-vector.jpg');  /* Replace with your image URL */
#             background-size: cover;
#         }
#    </style> """
#     ,
#     unsafe_allow_html=True
# )






# Configure and load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(
    page_title="Q&A Demo"
)
st.header("Conversational Q&A Chatbot")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User input and submit button
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# Process user input and display response
if submit_button and input_text:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")


