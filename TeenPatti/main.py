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


def trail(hand):
    if hand[0][1] == hand[1][1] == hand[2][1]:
        return(f"It's a trial: {hand}")


def pure_sequence(hand):
    denomination_list = [card[1] for card in hand]
    sorted_denominations = sorted(denomination_list, key=lambda x: denominations.index(x))
    if hand[0][0] == hand[1][0] == hand[2][0] \
        and sorted_denominations == denominations[denominations.index(sorted_denominations[0]):denominations.index(sorted_denominations[0]) + 3]:
        return (f"It's a pure sequence: {hand}")

def sequence(hand):
    denomination_list = [card[1] for card in hand]
    sorted_denominations = sorted(denomination_list, key=lambda x: denominations.index(x))
    if sorted_denominations == denominations[denominations.index(sorted_denominations[0]):denominations.index(sorted_denominations[0]) + 3]:
        return (f"It's a sequence: {hand}")

def color(hand):
    if hand[0][0] == hand[1][0] == hand[2][0]:
        return (f"It's a color: {hand}")

sample_hand = [['diamonds', '2'], ['diamonds', '2'], ['diamonds', '2']]

def pair(hand):
    if hand[0][1] == hand[1][1] or hand[0][1] == hand[2][1] or hand[1][1] == hand[2][1]:
        if not trail(hand):
            return (f"It's a pair: {hand}")


print()

print(f"player hand is: {sorted_player_hand}")
print(f"computer hand is: {sorted_comp_hand}")     

print()

if trail(sorted_player_hand):
    print(f"Player got a trail: {sorted_player_hand}")
if trail(sorted_comp_hand):
    print(f"computer got a trail: {sorted_comp_hand}")
if pure_sequence(sorted_player_hand):
    print(f"Player got a pure sequence: {sorted_player_hand}")
if pure_sequence(sorted_comp_hand):
    print(f"computer got a pure sequence: {sorted_comp_hand}")
if sequence(sorted_player_hand):
    print(f"Player got a sequence: {sorted_player_hand}")
if sequence(sorted_comp_hand):
    print(f"computer got a sequence: {sorted_comp_hand}")
if color(sorted_player_hand):
    print(f"Player got a color: {sorted_player_hand}")
if color(sorted_comp_hand):
    print(f"computer got a color: {sorted_comp_hand}")
if pair(sorted_player_hand):
    print(f"Player got a pair: {sorted_player_hand}")
if pair(sorted_comp_hand):
    print(f"computer got a pair: {sorted_comp_hand}")


def winner(player_hand, comp_hand):
    if trail(player_hand) and trail(comp_hand):
        print("It's a tie")
    elif trail(player_hand):
        print(f"Player won: {player_hand}")
    elif trail(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif pure_sequence(player_hand) and pure_sequence(comp_hand):
        print("It's a tie")
    elif pure_sequence(player_hand):
        print(f"Player won: {player_hand}")
    elif pure_sequence(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif sequence(player_hand) and sequence(comp_hand):
        print("It's a tie")
    elif sequence(player_hand):
        print(f"Player won: {player_hand}")
    elif sequence(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif color(player_hand) and color(comp_hand):
        print("It's a tie")
    elif color(player_hand):
        print(f"Player won: {player_hand}")
    elif color(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif pair(player_hand) and pair(comp_hand):
        print("It's a tie")
    elif pair(player_hand):
        print(f"Player won: {player_hand}")
    elif pair(comp_hand):
        print(f"Computer won: {comp_hand}")
    else:
        if sorted_player_hand > sorted_comp_hand:
            print(f"Player won: {player_hand}")
        elif sorted_player_hand < sorted_comp_hand:
            print(f"Computer won: {comp_hand}")
        else:
            print("It's a tie")
    


winner(sorted_player_hand, sorted_comp_hand)





