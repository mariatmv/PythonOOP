from project.card.card import Card


class CardRepository:
    count: int
    cards: list

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        try:
            existing_card = [x for x in self.cards if card.name == x.name][0]
            raise ValueError(f"Card {card.name} already exists!")
        except IndexError:
            self.cards.append(card)
            self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        needed_card = [x for x in self.cards if x.name == card][0]
        self.cards.remove(needed_card)
        self.count -= 1

    def find(self, name: str):
        needed_card = [x for x in self.cards if x.name == name][0]
        return needed_card
