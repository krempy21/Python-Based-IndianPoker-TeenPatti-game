class Card:
    def __init__(self, suit, denomination):
        self.suit = suit
        self.denomination = denomination

    def __str__(self):
        return self.denomination["denomination"] + " of " + self.suit

