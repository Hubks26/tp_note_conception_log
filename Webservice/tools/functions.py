import requests

def getNewID(): 
	req = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
	json = req.json()
	return(json["deck_id"])

def DrawCards(nbCards, deckID):
	if deckID == "" : 
		deckID = getNewID()

	req = requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count={}".format(deckID, nbCards))
	json = req.json()
	res = {"deck_id": json["deck_id"], "cards": json["cards"]}
	return(res)
