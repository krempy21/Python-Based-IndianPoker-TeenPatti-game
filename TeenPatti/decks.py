import random
from cards import Card


class Deck:

    def __init__(self):

        self.cards = []
        suits = ["hearts", "clubs", "spades", "diamonds"]
        
        denomination= ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        # sorted_strings = sorted(denomination, key=lambda x: denomination.index(x))
        # for string in sorted_strings:
            # return string

        for suit in suits:
            for denomination in denomination:
                self.cards.append(Card(suit, denomination))

    def shuffle(self):
        if len(self.cards) >= 2:
            random.shuffle(self.cards)

    def deal(self, number):

        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt



if __name__ == "__main__":
    # Create a new deck
    deck = Deck()

    # Print the initial deck
    print("Initial deck:")
    for card in deck.cards:
        print(card)

    # Shuffle the deck
    deck.shuffle()
    print("\nShuffled deck:")
    for card in deck.cards:
        print(card)

    # Deal some cards and print the dealt cards
    num_dealt_cards = 5
    dealt_cards = deck.deal(num_dealt_cards)
    print(f"\nDealt {num_dealt_cards} cards:")
    for card in dealt_cards:
        print(card)

    # Print the remaining cards in the deck
    print("\nRemaining cards in the deck:")
    for card in deck.cards:
        print(card)


