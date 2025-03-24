--VAŽNO ZA POKRETANJE I KORIŠĆENJE APLIKACIJE--

Prije svega, potrebno je zatim odraditi komandu:
$ pip install -r requirements.txt
kako bi se mogle instalirati sve neophodne komponente za pokretanje tekuće programske cjeline.

Neophodno je zatim u .env fajlu, koji se nalazi u putanji "legal-advisor-ai"/bekend da se postavi OpenAI API ključ, koji je validan i može obaviti konekciju sa željenim GPT modelom bez problema, e.g. OPEN_API_KEY=sk-proj-********* etc. (gdje nema razmaka i gdje je ključ napisan kao jedna riječ, bez navodnika, običan tekst se stavi u jednu liniju, bez znakova za novi red).

Za pokretanje ovog programske cjeline, neophodno je da se prvo pokrene fajl main.py, tako što će se, u terminalu VS-Code, kada se pozicionira u "legal advisor ai" folder i to prateći sljedeće korake:

1. cd bekend
2. uvicorn main:app --reload

Nakon toga, treba da se otvori novi terminal i u primarni root direktorijum "legal-advisor-ai" pokrenuti frontend UI interfejs, koristeći sljedeće komande:

1. cd frontend
2. streamlit run korisnicki_interfejs.py

Kada se ovi koraci ispune, potrebno je da se aplikacija koristi na način što će se postaviti pitanje u input polje, koje je pravnog tipa (npr. "what are my rights if I get pulled over by police officer?"), na koje će OpenAI GPT model odgovoriti.

--ARHITEKTURA APLIKACIJE LEGAL ADVISOR AI--

Ova aplikacija je implementirana koristeći FastAPI za bekend i Streamlit za frontend, a još važnije jeste istaknuti da se koristio OpenAI API za generisanje pravnih savjeta upotrebom GPT-3.5-Turbo modela. Sastoji se iz dva glavna dijela:

1. bekend, koji rukovodi API pozivima i komunikacijom sa OpenAI GPT modelom, kao i
2. frontend, koji omogućava UI korisnički interfejs.

--Struktura direktorijuma

📁 Legal Advisor AI/
├── 📄 README.md
├── 📄 requirements.txt
├── 📁 bekend/
│   ├── 📁 __pycache__/
│   ├── 📄 .env
│   ├── 📄 main.py
│   └── 📄 openai_api_konekcija.py
└── 📁 frontend/
    └── 📄 korisnicki_interfejs.py

--Detaljna analiza arhitekture

Bekend dio zadužen je za komunikaciju između korisnika i OpenAI API-ja. Sastavljen je iz main.py fajla i openai_api_konekcija.py fajla. 

Opis main.py fajla:

+ Koristi FastAPI za izgradnju RESTful API-ja;
+ Definiše krajnju tačku /chat koji prihvata pravno pitanje i prosljeđuje ga OpenAI-ju;
+ Za validaciju korisničkog unosa koristi Pydantic (preciznije BaseModel);
+ Vraća HTTP izuzetak (grešku) koda 500 (značenja: Internal Server Error) u slučaju da OpenAI API ne bude bio u mogućnosti da odgovori.

Opis openai_api_konekcija.py fajla:

+ Upotrebom dotenv biblioteke, učitava API ključ iz .env fajla;
+ Kreira sesiju sa OpenAI GPT-3.5-Turbo modelom;
+ Postavlja sistemsku ulogu AI modela kao pravnog savjetnika;
+ U cilju što preciznijih odgovora, postavlja se vrijednost temperature na 0.3;
+ Ispisuje log i vraća traceback informacije o grešci u slučaju greške u komunikaciji sa OpenAI-jem.

Frontend dio omogućava korisniku da unese pitanje i dobije odgovor od OpenAI GPT modela.

Opis korisnicki_interfejs.py:

+ Streamlit se koristi za izradu jednostavnog UI-a;
+ Korisnik unosi pravno pitanje u text_input polje;
+ Klikom na dugme "Pošalji", API se poziva i prikazuje odgovor GPT modela;
+ U st.session_state.chat_history se čuva istorija ćaskanja korisnika i GPT modela;
+ Omogućava sidebar sa informacijama o aplikaciji i više button image widget-a koji vode ka  eksternim linkovima (a to su AI alati, kao što su ChatGPT, Claude, Grok, Mistral);
+ UI ima dugmad "Korisno" i "Nije korisno".

**Koraci funkcionisanja aplikacije:

1. Korisnik unosi pravno pitanje u text_input polje Streamlit UI-ja;
2. Frontend utemeljen u korisnicki_interfejs.py šalje HTTP POST zahtjev ka bekendu main.py;
3. Bekend dobija pitanje i prosljeđuje ga OpenAI GPT-3.5-Turbo modelu (u fajlu openai_api_konekcija.py);
4. OpenAI vraća odgovor, koji bekend šalje nazad frontend aplikaciji;
5. Frontend prikazuje odgovor korisniku i nadovezuje istoriju razgovoru, shodno količini pitanja.

--PRISTUP LEGAL ADVISOR KONTEKSTU--

Cilj je bio omogućiti korisnicima da dobiju brze i precizne odgovore na njihove pravne nedoumice upotrebom vještačke inteligencije. 

Zarad rješavanja ovog problema, korišćen je OpenAI GPT-3.5-Turbo modela, koji je podešen da odgovara u profesionalnom (formalnom) tonu kao pravnik, koji bi pružao egzaktne (precizne) i koncizne pravne savjete, kao i da izbjegava upotrebu tematike iz drugih nauka, kao što su finansije, medicina i slično, radi postizanja što konkretnijeg i utemeljenijeg odgovora vezanih za oblast prava.

Upotrebom temperature (argumenta kreiranja objekta OpenAI modela) i postavljanja njene vrijednosti na 0.3 se utvrđuje da će odgovori pravnog savjetnika zasnovanog na vještačkoj inteligenciji biti precizniji i tačni u pravnom izražavanju, a ne kreativni. Takođe, ograničili smo max_token na 500 (takođe argument kreiranja objekta OpenAI modela), što predstavlja sasvim dovoljno karaktera za postavljanje konkretnog odgovora sa većom preciznošću u pravničkom izlaganju.

--IZAZOVI I SOLUCIJE--

Izazovi su redosljedno predstavljeni u nastavku:

1. Sigurnost API ključa
2. Ograničavanje uloga AI modela
3. Error handling (Upravljanje greškama)
4. API nevalidnost u procesu konekcije sa OpenAI modelima

Za ove izazove rješenja su prikazana istim redosljedom kao i izazovi:

1. Pošto API zbog sigurnosnih razloga ne smije da stoji unutar programskog koda zbog bezbjednosnih razloga, uveden je .env fajl za čuvanje ključa, učitan pomoću dotenv biblioteke, konkretno load_dotenv() i OPENAI_API_KEY = os.getenv("OPENAI_API_KEY");
2. Kako bi usmjerili GPT model da ne bude opširan u izlaganju, nego da konkretno izlaže svoje pravne odgovore, postavljena je temperatura na 0.3 kako bi preciznost odgovora bila na nivou i ograničili max_token na 500 kako bi omogućili pravni angažman bude istaknut u razgovoru sa korisnikom.
3. Dešavaju se greške u konekciji sa OpenAI API-ju, stoga je dodata try-except struktura koja omogućava hvatanje grešaka i njihov ispis na uvid korisniku u UI. Takođe, uveden je HTTP try-except blok koji radi u slučaju da OpenAI ne bude bio u stanju da odgovori (kod 500 - Internal Server Error).
4. U realizaciji ove aplikacije, OpenAI API ključ koji je prvobitno bio obezbijeđen za rješavanje ovog zadatka je bio, nažalost, nevalidan kada se ova aplikacija prvi put pokrenula. U cilju izlaska iz ovog problema, pribavio sam drugi OpenAI API ključ, za koji je trebao model da se promijeni (prvobitno sam koristio gpt-4, pa onda gpt-3.5-turbo u inicijalizaciji openAI objekta). Nakon promjene modela, dobio sam grešku 429 od strane OpenAI servera, koji podrazumijeva da je potrebno da se finansijski pretplatim kako bih mogao nastaviti sa konekcijom sa openAI GPT modelom: ovo služi kao dokaz da je konekcija protekla dobro sa OpenAI API-jem i da je u opticaju bio validan OpenAI API ključ, GPT model bi vratio željeni odgovor.

--MOJI DOPRINOSI I DOPRINOSI CLAUDE AI U IZRADI CJELOKUPNOG KODA--

Razvoj Legal Advisor AI aplikacije bio je izazovan i edukativan proces. Claude AI mi je pomogao u implementaciji RESTful API-ja koristeći FastAPI, kao i u razumIJevanju rukovanja greškama putem HTTPException. Takođe, uz njegovu pomoć savladao sam korišćenje st.session_state za čuvanje istorije razgovora u korisničkom interfejsu i safe_allow_html za formatirani prikaz sadržaja.

Samostalno sam istražio OpenAI API, kreirao objekat i konfigurisao model za obradu pravnih upita. U frontend dijelu, kroz Streamlit dokumentaciju, upoznao sam se sa dodavanjem emoji simbola, input polja, sidebar-a i dugmadi, a za stilizaciju sam se oslanjao na prethodno znanje iz HTML-a, CSS-a i Djanga, stečeno tokom mog prethodnog razvoja aplikacije za kardiologiju (KardiologAI).

Kombinovanjem naučenog i postojećeg iskustva uspješno sam razvio aplikaciju koja omogućava interaktivno pružanje pravnih savjeta.
