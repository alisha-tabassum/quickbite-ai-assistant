import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key = os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash-lite")

faq_content = open("faq.txt", "r", encoding= "utf-8").read()

st.set_page_config(page_title = "QuickBite AI Assisstant", page_icon= "🍔", layout= "centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@600;800&family=Poppins:wght@400;500&display=swap');

.stApp {
    background-image: 
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Ctext x='10' y='40' font-size='40' opacity='0.1'%3E%F0%9F%8D%94%3C/text%3E%3Ctext x='150' y='90' font-size='35' opacity='0.1'%3E%F0%9F%8D%95%3C/text%3E%3Ctext x='60' y='160' font-size='38' opacity='0.1'%3E%F0%9F%8D%9F%3C/text%3E%3Ctext x='200' y='200' font-size='36' opacity='0.1'%3E%F0%9F%A5%A4%3C/text%3E%3Ctext x='30' y='260' font-size='34' opacity='0.1'%3E%F0%9F%8D%9D%3C/text%3E%3C/svg%3E"),
        linear-gradient(135deg, #FF6B6B 0%, #FF8E53 25%, #FE6B8B 50%, #C062F0 75%, #6A3093 100%);
    background-repeat: repeat, no-repeat;
    background-size: 300px 300px, 300% 300%;
    background-position: 0 0, 0% 50%;
    background-attachment: fixed, fixed;
    animation: gradientShift 12s ease infinite;
    font-family: 'Poppins', sans-serif;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

[data-testid="stAppViewContainer"] {
    min-height: 100vh;
}

[data-testid="stChatInput"] textarea {
    background-color: rgba(255, 255, 255, 0.857) !important;
    border-radius: 20px !important;
    color: #333 !important;
}

[data-testid="stChatInput"] {
    border-radius: 20px !important;
}

h1 {
    font-family: 'Baloo 2', cursive;
    color: #7A1F00;
    text-align: center;
    font-size: 3.2em !important;
    text-shadow: 2px 2px 0px rgba(255,255,255,0.4);
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    color: #5C2E00;
    margin-bottom: 25px;
    font-weight: 500;
}

.stChatMessage {
    border-radius: 18px;
    padding: 10px;
    margin-bottom: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

[data-testid="stChatMessageContent"] {
    font-family: 'Poppins', sans-serif;
}

.stChatInput {
    border-radius: 25px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🍔 QuickBite AI Assistant 🍕</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your friendly food delivery helper — ask about orders, refunds, hours & more! 🛵💨</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🍔"
    with st.chat_message(message["role"], avatar=avatar):
        st.write(message["content"])

user_question = st.chat_input("Type you Question here... ")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    with st.chat_message("user", avatar="🧑"):
        st.write(user_question)

    with st.chat_message("assistant", avatar="🍔"):
        with st.spinner("🍔 QuickBite is thinking..."):
            prompt = f"Answer the question using only FAQ info: \n {faq_content} \n\n Question: {user_question}"
            try:
                response = model.generate_content(prompt)
                answer = response.text
            except Exception as e:
                answer = "Sorry, I'm having trouble responding right now. Please try again in a moment! 🙏"
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})


