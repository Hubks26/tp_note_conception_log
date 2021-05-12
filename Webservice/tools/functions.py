import requests

def getNewID(): 
	req = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
	json = req.json()
	return(json["deck_id"])

def DrawCards(deckID, nbCards):
	if not deckID: 
		deckID = getNewID()
	if nbCards < 0:
		nbCards = 0

	req = requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count={}".format(deckID, nbCards))
	return req.json()
