import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Google Gemini model
chat_model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

# Custom Prompt Placeholder
CUSTOM_PROMPT = """
When asked about identity or other related queries, the chatbot will:
Respond in a neutral, helpful manner.
Avoid explicitly stating that it's a chatbot by Google or based on Google/Gemini directly.
Mention it’s made by Bahul Kansal when asked about its creation.

Remmber:Answer the user's question in a clear, concise, and engaging manner.
"""

def generate_response(user_prompt):
    """
    Generate a response using Google Gemini with a custom prompt.
    
    Args:
        user_prompt (str): The user's query.

    Returns:
        str: The AI-generated response.
    """
    full_prompt = f"{CUSTOM_PROMPT}\n\nUser: {user_prompt}\nAI:"
    try:
        response = chat_model.predict(full_prompt)
        return response
    except Exception as e:
        return f"Sorry, an error occurred: {e}"

# Streamlit App
def main():
    st.set_page_config(page_title="General Chatbot", layout="wide")
    st.title("Bahul's Chatbot: Ask Anything!")

    # Text Input for User's Query
    user_input = st.text_input("Enter your question:")
    st.write("You can ask about any topic, and I will try to help!")

    if user_input:
        with st.spinner("Generating response..."):
            response = generate_response(user_input)
            st.write("**Response:**", response)

if __name__ == "__main__":
    main()
