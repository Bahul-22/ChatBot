import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configure model
model = genai.GenerativeModel("models/gemini-1.5-flash")


# Custom system prompt
CUSTOM_PROMPT = """
When asked about identity or other related queries, the chatbot will:
- Respond in a neutral, helpful manner.
- Avoid explicitly stating that it's a chatbot by Google or based on Google/Gemini directly.
- Mention it’s made by Bahul Kansal when asked about its creation.

Remember: Answer the user's question in a clear, concise, and engaging manner.
"""

def stream_response(prompt):
    full_prompt = f"{CUSTOM_PROMPT}\n\nUser: {prompt}\nAI:"
    try:
        response = model.generate_content(full_prompt, stream=True)
        return response
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Streamlit UI
def main():
    st.set_page_config(page_title="Bahul's Chatbot", layout="wide")
    st.title("🤖 Bahul's Chatbot: Ask Anything!")

    user_input = st.text_input("Enter your question:")
    if user_input:
        st.write("**Response:**")
        with st.spinner("Thinking..."):
            response = stream_response(user_input)
            if response:
                # Stream output token by token
                full_reply = ""
                response_area = st.empty()
                for chunk in response:
                    content = chunk.text
                    full_reply += content
                    response_area.markdown(full_reply)

if __name__ == "__main__":
    main()
