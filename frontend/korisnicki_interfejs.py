import streamlit as st
import requests

# Backend API URL
API_URL = "http://127.0.0.1:8000/chat"

# Funkcija za slanje upita bekendu
def get_legal_advice(question):
    response = requests.post(API_URL, json={"question": question})
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Unable to get a response from the server."

# UI dizajn
st.set_page_config(page_title="Legal Advisor AI", page_icon="⚖️", layout="centered")

# Naslov aplikacije
st.title("⚖️ Legal Advisor AI Chatbot")
st.markdown("Postavite pravno pitanje i dobijte odgovor od AI pravnog savetnika.")

# Memorija razgovora (istorija pitanja i odgovora)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input polje za korisnička pitanja
user_input = st.text_input("📝 Unesite svoje pravno pitanje:")

if st.button("📨 Pošalji"):
    if user_input.strip():
        with st.spinner("⏳ AI analizira vaše pitanje..."):
            ai_response = get_legal_advice(user_input)
        
        st.session_state.chat_history.append(("Vi", user_input))
        st.session_state.chat_history.append(("Legal Advisor AI", ai_response))
    

st.markdown("### 📜 Istorija razgovora:")
for role, text in st.session_state.chat_history:
    if role == "Vi":
        st.markdown(f"**🧑‍💼 {role}:** {text}")
    else:
        st.markdown(f"**🤖 {role}:** {text}")

        col1, col2 = st.columns([1, 1])
        with col1:
            st.button("👍", key=f"like_{text}")
        with col2:
            st.button("👎", key=f"dislike_{text}")

if st.button("🗑️ Resetuj razgovor"):
    st.session_state.chat_history = []

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
