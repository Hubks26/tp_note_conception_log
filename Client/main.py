import requests
from tools.functions import countCards

url = "http://127.0.0.1:8000"

if __name__ == '__main__':
	req = requests.get(url+"/create_deck")
	deckID = req.json()["deck_id"]
	print("L'identifiant du deck créé est : " + deckID + "\n")

	req = requests.post(url + "/draw_cards/10", json={"deck_id": deckID})
	cards = req.json()["cards"]
	print("Les cartes tirées sont :")
	print([card["code"] for card in cards])
	print("\nLe compte des cartes est :")
	print(countCards(cards))