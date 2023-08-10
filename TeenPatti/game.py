from hands import sorted_player_hand, sorted_comp_hand
from ranks_tp import trail, pure_sequence, sequence, color, pair, high_card

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
        print (high_card(player_hand, comp_hand))
    elif trail(player_hand):
        print(f"Player won: {player_hand}")
    elif trail(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif pure_sequence(player_hand) and pure_sequence(comp_hand):
        print(high_card(player_hand, comp_hand))
    elif pure_sequence(player_hand):
        print(f"Player won: {player_hand}")
    elif pure_sequence(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif sequence(player_hand) and sequence(comp_hand):
        print(high_card(player_hand, comp_hand))
    elif sequence(player_hand):
        print(f"Player won: {player_hand}")
    elif sequence(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif color(player_hand) and color(comp_hand):
        print(high_card(player_hand, comp_hand))
    elif color(player_hand):
        print(f"Player won: {player_hand}")
    elif color(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif pair(player_hand) and pair(comp_hand):
        print(high_card(player_hand, comp_hand))
    elif pair(player_hand):
        print(f"Player won: {player_hand}")
    elif pair(comp_hand):
        print(f"Computer won: {comp_hand}")
    elif high_card(player_hand, comp_hand):
        if player_hand > comp_hand:
            print(f"Player won: {player_hand}")
        else:
            print(f"Computer won: {comp_hand}")
    else:
        print("It's a tie")
