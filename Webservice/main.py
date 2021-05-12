from fastapi import FastAPI
from tools.functions import getNewID, DrawCards
from tools.CardSelector import CardSelector

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Bienvenue sur le webservice !"}

@app.get("/create_deck/")
async def get_id(): 
	deckID = getNewID()
	return {"deck_id" : deckID}

@app.post("/draw_cards")
def draw(cs : CardSelector):
	res = DrawCards(cs.nbCards, cs.DeckID)
	return(res)