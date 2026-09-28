import streamlit as st
from googletrans import Translator
import json

# Initialize translator
translator = Translator()

# Function to generate bot response with translation
def chatbot_response(message, lang='en'):
    translated = translator.translate(message, dest='en').text
    reply = f"You said (translated to English): {translated}"
    return translator.translate(reply, dest=lang).text

# Save chat history to file
def save_history():
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.chat_history, f, ensure_ascii=False, indent=2)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# App title
st.title("💬 Multilingual Campus Chatbot")

# Language selector
lang = st.selectbox("Choose your language:", ["en", "hi", "te"])

# Display chat history
for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")

# User input
user_input = st.text_input("Type your message:", key="input")

if user_input:
    bot_reply = chatbot_response(user_input, lang)
    st.session_state.chat_history.append({"user": user_input, "bot": bot_reply})
    save_history()
    st.experimental_rerun()

# Clear history button
if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    save_history()
    st.experimental_rerun()