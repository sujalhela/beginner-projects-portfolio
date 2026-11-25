"""A simple command-line AI chatbot using the OpenAI Responses API.

Setup:
    pip install -r requirements.txt
    Set OPENAI_API_KEY in your environment
    python chatbot.py
"""

import os
from openai import OpenAI, OpenAIError


INSTRUCTIONS = (
    "You are a friendly, clear assistant for a beginner learning Python, "
    "technology, and data analysis. Explain concepts simply, use examples "
    "when helpful, and be honest when you are unsure."
)


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Missing OPENAI_API_KEY.")
        print("Set your API key as an environment variable, then run again.")
        return

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-5.5")
    previous_response_id = None

    print("Beginner AI Chatbot")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("-" * 40)

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_text:
            continue

        if user_text.lower() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break

        request = {
            "model": model,
            "instructions": INSTRUCTIONS,
            "input": user_text,
        }
        if previous_response_id:
            request["previous_response_id"] = previous_response_id

        try:
            response = client.responses.create(**request)
            answer = response.output_text
            print(f"Bot: {answer or 'I could not generate a text response.'}\n")
            previous_response_id = response.id
        except OpenAIError as error:
            print(f"API request failed: {error}")
            print("Check your API key, account access, and connection.\n")


if __name__ == "__main__":
    main()
