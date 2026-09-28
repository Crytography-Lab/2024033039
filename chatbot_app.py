import streamlit as st

def chatbot_response(message):
    return f"You said: {message}"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💬 Multilingual Campus Chatbot")

for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")

user_input = st.text_input("Type your message:", key="input")

if user_input:
    bot_reply = chatbot_response(user_input)
    st.session_state.chat_history.append({"user": user_input, "bot": bot_reply})
    st.experimental_rerun()

if st.button("Clear Chat History"):
    st.session_state.chat_history = []
    st.experimental_rerun()
