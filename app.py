import os
import streamlit as st
from chatbot import chatbot_response

st.title("CDP Support Chatbot 🤖")
st.write("Ask me how to use Segment, mParticle, Lytics, or Zeotap!")

user_query = st.text_input("You: ", "")

if st.button("Ask"):
    response = chatbot_response(user_query)
    st.write(f"🤖: {response}")
