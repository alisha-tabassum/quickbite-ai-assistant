# 🍔 QuickBite AI Assistant

An AI chatbot that answers customer questions for a fictional food delivery business, using only the company's own FAQ data.

**Live demo:** [Try it here](https://quickbite-ai-assistant-e87vuunl4rsh5hb8sdzq4c.streamlit.app/)

## What it does

- Answers customer questions (delivery, refunds, payments, accounts) from a custom FAQ file
- Replies in a friendly chat style and handles greetings and small talk
- Stays on topic: if the answer isn't in the FAQ, it says so instead of making things up
- Keeps the conversation history on screen, like a real chat app
- Shows a friendly message instead of crashing if the AI service fails

## Tech stack

- **Python**
- **Streamlit** for the web interface
- **Google Gemini API** for generating answers
- **python-dotenv** for keeping the API key out of the code

## How it works

1. The app loads `faq.txt`, which holds 75+ questions and answers.
2. When a user asks something, the app sends the FAQ and the question to the Gemini model.
3. The model is told to answer only from the FAQ, so replies stay accurate to the business.
4. The answer appears in the chat window.

## Run it locally

1. Clone the repository and open the folder.
2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Create a file named `.env` in the project folder and add your Gemini API key (free from Google AI Studio):

```
GEMINI_API_KEY=your_key_here
```

4. Start the app:

```
streamlit run app.py
```

## Project structure

```
quickbite-ai-assistant/
├── app.py             # Streamlit app: UI and chat logic
├── faq.txt            # Business knowledge base
├── requirements.txt   # Python dependencies
└── .gitignore         # Keeps the API key out of GitHub
```

## Adapting it to another business

Replace the contents of `faq.txt` with any company's FAQ, policies or product information, and the chatbot will answer from that data instead.

## Author

Alisha Tabassum, Computer Engineer

[LinkedIn](www.linkedin.com/in/alisha-tabassum-2230452b0)


