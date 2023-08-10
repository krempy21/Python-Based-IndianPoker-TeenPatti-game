import random

print()
print("*" * 30)
print("Welcome to Teen Patti")
print("*" * 30)
print()


suits = ["hearts", "spades", "diamonds", "clubs"]
denominations = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
cards = []

for suit in suits:
    for denomination in denominations:
        cards.append([suit, denomination])

def sort(cards):
    rank_dict = {denomination: rank for rank, denomination in enumerate(denominations, start=1)}
    sorted_cards = sorted(cards, key=lambda card: (rank_dict.get(card[1], float('inf')), card[0], card[1]))
    return sorted_cards

def shuffle():
    random.shuffle(cards)

shuffle()

def deal():
    one_hand = []
    for i in range(3):
        card = cards.pop()
        one_hand.append(card)
    return one_hand

player_hand = deal()
comp_hand = deal()


sorted_player_hand = sort(player_hand)
sorted_comp_hand = sort(comp_hand)
