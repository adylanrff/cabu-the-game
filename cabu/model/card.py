import enum

class Symbol(enum.Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Suit(enum.Enum):
    DIAMOND = 1
    CLOVER = 2
    HEART = 3
    SPADE = 4

class Card(object):
    def __init__(self, symbol: Symbol, suit: Suit):
        self.symbol = symbol
        self.suit = suit

    def __lt__(self, other):
        if (self.suit.value < other.suit.value):
            return True
        elif (self.suit.value == other.suit.value):
            if (self.symbol.value < self.symbol.value):
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.suit == other.suit and self.symbol == other.symbol