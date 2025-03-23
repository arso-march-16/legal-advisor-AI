from fastapi import FastAPI, HTTPException # FastAPI - za pravljenje API u ovoj aplikaciji, HTTPException - za postavljanje izuzetka odnosno greške u konekciji sa OpenAI API
from pydantic import BaseModel # definiše model za ulazne podatke
from openai_api_konekcija import ask_openai_legal_advisor # uvoz funkcije iz openai_api_konekcija.py

app = FastAPI() # osnova postavljanja ruta u API strukturi preko FastAPI-ja 

# Model API zahtijeva da korisnički unos bude striktno string, što pydantic.BaseModel to temeljno provjerava
class ChatRequest(BaseModel):
    question: str

# u nastavku je API redirekcija u URL "/chat" stranicu kao odgovor na korisnički upit (prompt)
# obavlja se pokušaj pribavljanja odgovora, koji, u slučaju neuspjeha, vraća HTTP tip greške (kod 500) sa potrebnim specifikacijama greške u konekciji
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = ask_openai_legal_advisor(request.question) # odgovor funkcije na postavljeno korisničko pitanje... 
        return {"response": response} #... se vraća funkciji chat kao odgovor u vidu JSON formata
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

