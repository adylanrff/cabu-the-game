from typing import List, AnyStr

from model.card import Card


class Player:
    def __init__(self, name: AnyStr, score: AnyStr, card: List[Card]):
        self.name = name
        self.score = score
        self.card = card

    def add_card(self, card):
        self.card.append(card)

    def switch_card(self, old_card, new_card):
        for card in self.card:
            if card == old_card:
                card, new_card = new_card, card