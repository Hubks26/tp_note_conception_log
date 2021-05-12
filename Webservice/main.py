from fastapi import FastAPI
from tools.functions import getNewID, DrawCards
from tools.Deck import Deck

app = FastAPI()

@app.get("/")
async def root():
	return {"message": "Bienvenue sur le webservice !"}

@app.get("/create_deck")
async def getID(): 
	deckID = getNewID()
	return {"deck_id" : deckID}

@app.post("/draw_cards/{nbCards}")
async def draw(nbCards: int, deck: Deck):
	drawnCards = DrawCards(deck.deck_id, nbCards)
	res = {"deck_id": drawnCards["deck_id"], "cards": drawnCards["cards"]}
	return res 