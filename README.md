--VAŽNO ZA POKRETANJE I KORIŠĆENJE APLIKACIJE--

Za pokretanje ovog programske cjeline, neophodno je da se prvo pokrene fajl main.py, tako što će se, u terminalu VS-Code, kada se pozicionira u "legal advisor ai" folder i to prateći sljedeće korake:

1. cd bekend
2. uvicorn main:app --reload

Nakon toga, treba da se vrati u primarni root direktorijum i pokrenuti frontend UI interfejs, koristeći sljedeće komande:

1. cd ../
2. cd frontend
3. streamlit run korisnicki_interfejs.py

Kada se ovi koraci ispune, potrebno je da se aplikacija koristi na način što će se postaviti pitanje u input polje, koje je pravnog tipa (npr. "what are my rights if I get pulled over by police officer?"), na koje će OpenAI GPT model odgovoriti.

--ARHITEKTURA APLIKACIJE--

