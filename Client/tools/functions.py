def countCards(cards):
    counters = {"SPADES":0,"DIAMONDS":0,"CLUBS":0,"HEARTS":0}
    for card in cards : 
        counters[card["suit"]] += 1
    return counters
