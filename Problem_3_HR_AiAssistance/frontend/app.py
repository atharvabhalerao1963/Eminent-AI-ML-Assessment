import streamlit as st
import requests

API_URL = "http://localhost:8000/ask"

st.set_page_config(
    page_title="Enterprise HR Policy Assistant",
    page_icon="🤖"
)

st.title("🤖 Enterprise HR Policy Assistant")

question = st.text_input(
    "Ask an HR-related question"
)

if st.button("Get Answer"):

    if question:

        response = requests.post(
            API_URL,
            json={
                "question": question
            }
        )

        data = response.json()

        st.subheader("Answer")

        st.write(data["answer"])



      