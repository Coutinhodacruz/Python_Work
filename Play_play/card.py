deck = [x for x in range(52)]

suits = ["spades", "hearts", "diamond", "clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

import random

random.shuffle(deck)

for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("card number ", deck[i], "is the", rank, "of", suit)
