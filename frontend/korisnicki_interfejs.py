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
st.set_page_config(page_title="Legal Advisor AI", page_icon=":classical_building:", layout="centered")

# Naslov aplikacije
st.title(":male-judge: Legal Advisor AI Chatbot")
st.markdown("<div style='font-size:20px;color:yellow;'>Postavite pravno pitanje i dobijte odgovor od AI pravnog savjetnika.</div>",unsafe_allow_html=True)

# Memorija razgovora (istorija pitanja i odgovora)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input polje za korisnička pitanja
user_input = st.text_input(":memo: Unesite svoje pravno pitanje:", placeholder="Ovdje upišite Vaše pitanje...", help="Postavite pitanje koje se odnosi na pravne savjete.")

if st.button(":package: Pošalji"):
    if user_input.strip():
        with st.spinner(":timer_clock: AI analizira vaše pitanje..."):
            ai_response = get_legal_advice(user_input)
        
        st.session_state.chat_history.append(("Vi", user_input))
        st.session_state.chat_history.append(("Legal Advisor AI", ai_response))

# Naslov
st.divider()
st.markdown("<div style='text-align: center; font-size: 16px;'>Testirajte i druge GPT modele</div>",
    unsafe_allow_html=True)

# Kreiranje kolona za slike
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        """
        <a href='https://chatgpt.com/' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/chatgpt5223.logowik.com.webp' alt='GPT Model 1'  style='width:50%;height:auto;display:block;margin:auto;'>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <a href='https://www.claude.ai' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/claude4477.logowik.com.webp' alt='GPT Model 2'  style='width:50%;height:auto;display:block;margin:auto;'>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <a href='https://x.ai/' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/grok-ai1793.logowik.com.webp' alt='GPT Model 3'  style='width:50%;height:auto;display:block;margin:auto;'>
        </a>
        """,
        unsafe_allow_html=True,
    )

with col4:
    st.markdown(
        """
        <a href='https://chat.mistral.ai/chat' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/mistral-ai-20252037.logowik.com.webp' alt='GPT Model 4'  style='width:50%;height:auto;display:block;margin:auto;'>
        </a>
        """,
        unsafe_allow_html=True,
    )

st.divider()
    

st.markdown("### :mailbox_with_mail: Istorija razgovora:")
for role, text in st.session_state.chat_history:
    if role == "Vi":
        st.markdown(f"**:male-office-worker: {role}:** {text}")
    else:
        st.markdown(f"**:robot_face: {role}:** {text}")

# Dodavanje teksta povrh dugmadi za ocenjivanje
        st.markdown("<div style='color:orange; font-size:18px;'>Da li vam je ovaj odgovor bio koristan ili ne?</div>",unsafe_allow_html=True)
        
# Kreiranje dugmadi u istom redu sa minimalnim razmakom
        st.markdown(
            f"""
            <div style="display: flex; gap: 8px; align-items: center;">
                <button style="background-color: black; border: 1px solid white; border-radius: 5px; padding: 5px 10px; cursor: pointer;" onclick="document.getElementById('like_{text}').click()"> 👍 Korisno</button>
                <button style="background-color: black; border: 1px solid white; border-radius: 5px; padding: 5px 10px; cursor: pointer;" onclick="document.getElementById('dislike_{text}').click()">👎 Nije korisno</button>
            </div>
            """,
            unsafe_allow_html=True,
        )

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
