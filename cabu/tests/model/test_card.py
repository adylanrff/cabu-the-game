import unittest

from model.card import Card
from model.card import Symbol
from model.card import Suit

class TestCard(unittest.TestCase):
    def test_constructor(self):
        card = Card(Symbol.ACE, Suit.CLOVER)
        self.assertEqual(card.symbol, Symbol.ACE)
        self.assertEqual(card.suit, Suit.CLOVER)

if __name__ == '__main__':
    unittest.main()