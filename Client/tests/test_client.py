import unittest
import requests
from tools.functions import countCards

class TestClient(unittest.TestCase):
	def test_countCards(self):
		#Assume
		req = requests.get("https://deckofcardsapi.com/api/deck/new/")
		deckID = req.json()["deck_id"]
		req = requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=20".format(deckID))
		cards1 = req.json()["cards"]
		
		req = requests.get("https://deckofcardsapi.com/api/deck/new/")
		deckID = req.json()["deck_id"]
		req = requests.get("https://deckofcardsapi.com/api/deck/{}/draw/?count=52".format(deckID))
		cards2 = req.json()["cards"]

		#Action
		counts1 = countCards(cards1)
		counts2 = countCards(cards2)
		expected_results1 = {'SPADES': 13, 'DIAMONDS': 7, 'CLUBS': 0, 'HEARTS': 0}
		expected_results2 = {'SPADES': 13, 'DIAMONDS': 13, 'CLUBS': 13, 'HEARTS': 13}

		#Assert
		self.assertEqual(expected_results1, counts1)
		self.assertEqual(expected_results2, counts2)