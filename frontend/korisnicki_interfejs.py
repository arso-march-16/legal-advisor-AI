import streamlit as st
import requests

# Backend API URL
API_URL = "http://127.0.0.1:8000/chat"

# Funkcija za slanje upita bekendu, ukoliko je 200 (OK) kod u pitanju, onda se vraća odgovor u vidu JSON formata, u protivnom javlja grešku
def get_legal_advice(question):
    response = requests.post(API_URL, json={"question": question})
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error: Unable to get a response from the server."

# UI dizajn za tab stranice (aplikacije)
st.set_page_config(page_title="Legal Advisor AI", page_icon=":classical_building:", layout="centered")

# Naslov aplikacije
st.title(":male-judge: Legal Advisor AI Chatbot")
st.markdown("<div style='font-size:20px;color:yellow;'>Postavite pravno pitanje i dobijte odgovor od AI pravnog savjetnika.</div>",unsafe_allow_html=True)

# Memorija razgovora (istorija pitanja i odgovora)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input polje za korisnička pitanja
user_input = st.text_input(":memo: Unesite svoje pravno pitanje:", placeholder="Ovdje upišite Vaše pitanje...", help="Postavite pitanje koje se odnosi na pravne savjete.")
# klikom na dugme "Pošalji" spinner se pojavljuje koji daje uvid korisniku da se nešto dešava "iza scene"
# dobija se odgovor od strane AI servera i čuva se u istoriji ćaskanja i prikazuje na uvid korisniku
if st.button(":package: Pošalji"):
    if user_input.strip():
        with st.spinner(":timer_clock: AI analizira vaše pitanje..."):
            ai_response = get_legal_advice(user_input)
        
        st.session_state.chat_history.append(("Vi", user_input))
        st.session_state.chat_history.append(("Legal Advisor AI", ai_response))

# Sidebar sadržaj, sa ikonicama za odlazak na druge linkove (tačnije modele)
# uključena sekcija "O aplikaciji" i "Sva prava zadržana"
with st.sidebar:
    st.markdown(f"""
    <div style='text-align: center; padding: 15px 0;'>
        <h1 style='color: white;'>👨‍⚖️ Legal Advisor AI</h1>
        <h4 style='color: #E0E1DD;'>Vaš AI pravni savjetnik</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("## O aplikaciji")
    st.markdown("Legal Advisor AI vam pomaže da dobijete brze pravne savjete koristeći naprednu AI tehnologiju.")
    
    st.markdown("## Testirajte i druge modele")
    
    # Linkovi ka drugim AI modelima prikazani slikama u sidebar-u
    st.markdown("""
    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px;'>
        <a href='https://chatgpt.com/' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/chatgpt5223.logowik.com.webp' 
                 alt='ChatGPT' style='width:100%; border-radius: 8px;'>
        </a>
        <a href='https://www.claude.ai' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/claude4477.logowik.com.webp' 
                 alt='Claude' style='width:100%; border-radius: 8px;'>
        </a>
        <a href='https://x.ai/' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/grok-ai1793.logowik.com.webp' 
                 alt='Grok' style='width:100%; border-radius: 8px;'>
        </a>
        <a href='https://chat.mistral.ai/chat' target='_blank'>
            <img src='https://logowik.com/content/uploads/images/mistral-ai-20252037.logowik.com.webp' 
                 alt='Mistral' style='width:100%; border-radius: 8px;'>
        </a>
    </div>
                        <div style='text-align: center; padding: 20px 0; color: #aaa; font-size: 12px;'>
    © 2025 Legal Advisor AI | Sva prava zadržana | Ovo nije zamjena za profesionalni pravni savjet
</div>
    """, unsafe_allow_html=True)
    
# relacija korisnik-AI i prikaz istorije njihovog razgovora (pitanja i odgovori)
st.markdown("### :mailbox_with_mail: Istorija razgovora:")
for role, text in st.session_state.chat_history:
    if role == "Vi":
        st.markdown(f"**:male-office-worker: {role}:** {text}")
    else:
        st.markdown(f"**:robot_face: {role}:** {text}")

# Dodavanje teksta povrh dugmadi za ocjenjivanje
        st.markdown("<div style='color:orange; font-size:18px;'>Da li vam je ovaj odgovor bio koristan ili ne?</div>",unsafe_allow_html=True)
        
# Kreiranje dugmadi za like/dislike koja ne rade na njihov pritisak u istom redu sa minimalnim razmakom
        st.markdown(
            f"""
            <div style="display: flex; gap: 8px; align-items: center;">
                <button style="background-color: black; border: 1px solid white; border-radius: 5px; padding: 5px 10px; cursor: pointer;" onclick="document.getElementById('like_{text}').click()"> 👍 Korisno</button>
                <button style="background-color: black; border: 1px solid white; border-radius: 5px; padding: 5px 10px; cursor: pointer;" onclick="document.getElementById('dislike_{text}').click()">👎 Nije korisno</button>
            </div>
            """,
            unsafe_allow_html=True,
        )
# opšta podešavanja za cijeli dokument su u nastavku
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
