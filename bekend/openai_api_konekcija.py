from openai import OpenAI # biblioteka i funkcija prijeko potrebna za interakciju sa GPT modelom preko odgovarajućeg OpenAI API-ja
import os # biblioteka za manipulaciju nad fajlovima u Python-u
from dotenv import load_dotenv # biblioteka za učitavanje .env fajlova 
import traceback # koristi se za ispisivanje potencijalnih razloga za grešku u terminalu

# dobijanje i učitavanje OpenAI API ključa iz .env fajla
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# postavljanje greške u slučaju da API ključ nije bio postavljen u .env fajlu
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY nije pronađen. Postavi ga u .env fajl.")

klijent=OpenAI(api_key=OPENAI_API_KEY) # postavljanje objekta komunikacije sa gpt modelom

def ask_openai_legal_advisor(pitanje: str) -> str: # funkcija kreiranja pitanja i odgovora na relaciji korisnik-model
    # pokušava se u try bloku da se obavi konekcija sa OpenAI API 
    try:
        response = klijent.chat.completions.create( # kreiranje komunikacije izmedju GPT modela i korisnika
            model="gpt-3.5-turbo",  # koji se OpenAI-jev model koristi
            messages=[
                {"role": "system", "content": (
                    "You are a professional legal advisor. "
                    "Provide accurate and concise legal advice in a formal tone. "
                    "Do not offer medical, financial, or personal advice beyond legal matters."
                )}, # podešavanje uloge GPT modela, u smislu njegove struke, kakve odgovore da daje, u kakvom načinu govora, koja su mu ograničenja (limitations) 
                {"role": "user", "content": pitanje} # podešavanje uloge korisnika i pitanja na koje GPT model odgovara
            ],
            temperature=0.3,  # Niža temperatura omogućava preciznije odgovore, a veća kreativnije odgovore
            max_tokens=500 # podešavanje dužine odgovora GPT modela na korisničko pitanje (500 je za precizne odgovore sasvim dovoljno)
        )
        return response.choices[0].message.content # pristupa prvom izboru za odgovor i ispisuje ga
    except Exception as e: # ovaj blok predstavlja ispis izuzetka, odnosno razloge za greške u konekciji sa OpenAI API-jem
        error_trace=traceback.format_exc()
        print(f"Error connecting to OpenAI: {str(e)}")
        print(f"Full error: {error_trace}")
        return f"Error: {str(e)}"
