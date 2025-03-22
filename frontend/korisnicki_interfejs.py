import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

def get_legal_advice(pitanje):
    odgovor = requests.post(API_URL, json={"question": pitanje})
    if odgovor.status_code == 200:
        return odgovor.json()["response"]
    else:
        return "Greska: Neuspjesno dobijanje odgovora od servera!"

st.set_page_config(page_title="Legal Advisor AI", page_icon="⚖️", layout="centered")

st.title("⚖️ Legal Advisor AI Chatbot")
st.markdown("Postavite pravno pitanje i dobijte odgovor od AI pravnog savetnika.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("📝 Unesite svoje pravno pitanje:")

if st.button("📨 Pošalji"):
    if user_input.strip():
    
        ai_response = get_legal_advice(user_input)
        
        st.session_state.chat_history.append(("Vi", user_input))
        st.session_state.chat_history.append(("Legal Advisor AI", ai_response))

st.markdown("### 📜 Istorija razgovora:")
for role, text in st.session_state.chat_history:
    if role == "Vi":
        st.markdown(f"**🧑‍💼 {role}:** {text}")
    else:
        st.markdown(f"**🤖 {role}:** {text}")

st.markdown("""
<style>
    body {
        font-family: Arial, sans-serif;
    }
    .stTextInput, .stButton {
        width: 100%;
    }
    .stMarkdown {
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)
