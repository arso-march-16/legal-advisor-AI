--VAŽNO ZA POKRETANJE I KORIŠĆENJE APLIKACIJE--

Za pokretanje ovog programske cjeline, neophodno je da se prvo pokrene fajl main.py, tako što će se, u terminalu VS-Code, kada se pozicionira u "legal advisor ai" folder i to prateći sljedeće korake:

1. cd bekend
2. uvicorn main:app --reload

Nakon toga, treba da se otvori novi terminal i u primarni root direktorijum pokrenuti frontend UI interfejs, koristeći sljedeće komande:

1. cd frontend
2. streamlit run korisnicki_interfejs.py

Kada se ovi koraci ispune, potrebno je da se aplikacija koristi na način što će se postaviti pitanje u input polje, koje je pravnog tipa (npr. "what are my rights if I get pulled over by police officer?"), na koje će OpenAI GPT model odgovoriti.

--ARHITEKTURA APLIKACIJE LEGAL ADVISOR AI--

Ova aplikacija je implementirana koristeći FastAPI za bekend i Streamlit za frontend, a još važnije jeste istaknuti da se koristio OpenAI API za generisanje pravnih savjeta upotrebom GPT-3.5-Turbo modela. Sastoji se iz dva glavna dijela:

1. bekend, koji rukovodi API pozivima i komunikacijom sa OpenAI GPT modelom, kao i
2. frontend, koji omogućava UI korisnički interfejs.

--Struktura direktorijuma

>Legal Advisor AI folder
-->> README.md
-->> requierements.txt
-->> bekend folder
---->>> pycache folder
---->>> .env fajl
---->>> main.py fajl
---->>> openai_api_konekcija.py fajl
-->> frontend
---->>> korisnicki_interfejs.py

--Detaljna analiza arhitekture

Bekend dio zadužen je za komunikaciju između korisnika i OpenAI API-ja. Sastavljen je iz main.py fajla i openai_api_konekcija.py fajla. 

Opis main.py fajla:

+ Fajl obavlja koristi FastAPI za izgradnju RESTful API-ja,
+ Definiše krajnju tačku /chat koji prihvata pravno pitanje i prosljeđuje ga OpenAI-ju,
+ Za validaciju korisničkog unosa koristi Pydantic (preciznije BaseModel),
+ Vraća HTTP izuzetak (grešku) koda 500 (značenja: Internal Server Error) u slučaju da OpenAI API ne bude bio u mogućnosti da odgovori.

Opis openai_api_konekcija.py fajla:

+ Upotrebom dotenv biblioteke, učitava API ključ iz .env fajla,
+ Kreira sesiju sa OpenAI GPT-3.5-Turbo modelom,
+ Postavlja sistemsku ulogu AI modela kao pravnog savjetnika,
+ U cilju što preciznijih odgovora, postavlja se vrijednost temperature na 0.3,
+ Ispisuje log i vraća traceback informacije o grešci u slučaju greške u komunikaciji sa OpenAI-jem.

Frontend dio omogućava korisniku da unese pitanje i dobije odgovor od OpenAI GPT modela.

Opis korisnicki_interfejs.py:

+ Streamlit se koristi za izradu jednostavnog UI-a,
+ Korisnik unosi pravno pitanje u text_input polje,
+ Klikom na dugme "Pošalji", API se poziva i prikazuje odgovor GPT modela,
+ U st.session_state.chat_history se 



