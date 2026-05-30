import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

deck = [(rank, suit) for suit in suits for rank in ranks]

card = random.choice(deck)

print("Drawn Card:", card[0], "of", card[1])

if card[1] == "Hearts":
    print("The card is a HEART.")
else:
    print("The card is NOT a HEART.")
