"""A small browser-based chatbot built with Streamlit and the OpenAI API.

Run from the repository root:
    streamlit run python/ai-chatbot/streamlit_app.py
"""

import os

import streamlit as st
from openai import OpenAI, OpenAIError


st.set_page_config(page_title="Beginner AI Chatbot", page_icon="🤖")
st.title("🤖 Beginner AI Chatbot")
st.caption("A learning project built with Python, Streamlit, and the OpenAI Responses API.")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY is not set. Add it to your environment before starting the app.")
    st.code('$env:OPENAI_API_KEY="your_api_key_here"  # Windows PowerShell\n'
            'export OPENAI_API_KEY="your_api_key_here"  # macOS / Linux')
    st.stop()

client = OpenAI(api_key=api_key)
model = os.getenv("OPENAI_MODEL", "gpt-5.5")
instructions = (
    "You are a friendly assistant for a beginner learning Python, technology, "
    "and data analysis. Explain concepts simply, give examples when helpful, "
    "and be honest when you are unsure."
)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

with st.sidebar:
    st.subheader("About this project")
    st.write("A simple multi-turn chatbot interface. Messages are sent to the OpenAI API.")
    st.caption(f"Model setting: {model}")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.session_state.previous_response_id = None
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me something...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    request = {
        "model": model,
        "instructions": instructions,
        "input": prompt,
    }
    if st.session_state.previous_response_id:
        request["previous_response_id"] = st.session_state.previous_response_id

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.responses.create(**request)
                answer = response.output_text or "I could not generate a text response."
                st.markdown(answer)
                st.session_state.previous_response_id = response.id
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except OpenAIError as error:
                st.error(f"The API request failed: {error}")
                st.info("Check your API key, API access, usage limits, and internet connection.")
