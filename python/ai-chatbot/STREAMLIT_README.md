# Browser AI Chatbot (Streamlit)

This is a small browser-based interface for the beginner chatbot project. It uses Streamlit for the UI and the official OpenAI Python SDK for responses.

## Features

- Chat interface in a web browser
- Multi-turn context using the previous response ID
- Clear conversation button
- API key read from an environment variable (never stored in source code)

## Requirements

- Python 3.10+
- An OpenAI API key with API access and available usage/billing

## Install

From the repository root:

```bash
pip install -r requirements.txt
```

## Set your API key

**Windows PowerShell:**

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**macOS / Linux:**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Never paste your API key into this repository or commit it to GitHub.

## Run the app

From the repository root:

```bash
streamlit run python/ai-chatbot/streamlit_app.py
```

Streamlit will print a local URL (usually `http://localhost:8501`) to open in your browser.

Optional model override: set the `OPENAI_MODEL` environment variable to a model available to your API account. The default in this example is `gpt-5.5`.

## How it works

1. Streamlit collects a message from the chat input.
2. The app sends the message to the OpenAI Responses API.
3. It displays the generated answer.
4. It passes the previous response ID on the next turn to continue the conversation.

## Notes

- API usage may incur charges; check current API pricing and usage limits.
- This is an educational prototype, not a production-ready application.
- Do not send sensitive personal or confidential information.
