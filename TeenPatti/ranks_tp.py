from hands import denominations
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

def rank_value(rank):
    if rank.isdigit():
        return int(rank)
    elif rank == 'A':
        return 14
    elif rank == 'K':
        return 13
    elif rank == 'Q':
        return 12
    elif rank == 'J':
        return 11

def high_card(hand1, hand2):
    max_rank_hand1 = max(hand1, key=lambda card: rank_value(card[1]))
    max_rank_hand2 = max(hand2, key=lambda card: rank_value(card[1]))

    if rank_value(max_rank_hand1[1]) > rank_value(max_rank_hand2[1]):
        return f"hand 1 won: {hand1}"
    elif rank_value(max_rank_hand1[1]) < rank_value(max_rank_hand2[1]):
        return f"hand 2 won: {hand2}"
    else:
        return "It's a tie"