import unittest
from src.card import Card, Deck

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts', 'A')

    def test_card_initialization(self):
        self.assertEqual(self.card.suit, 'Hearts', 'The suit should be Hearts')
        self.assertEqual(self.card.value, 'A', 'The value should be A')

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52, 'A new deck should have 52 cards')

    def test_shuffle_deck(self):
        cards_before_shuffle = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(self.deck.cards, cards_before_shuffle, 'The deck should be shuffled')

    def test_deal_card(self):
        initial_deck_length = len(self.deck.cards)
        dealt_card = self.deck.deal()
        self.assertIsInstance(dealt_card, Card, 'Dealt card should be instance of Card class')
        self.assertEqual(len(self.deck.cards), initial_deck_length - 1, 'The deck should have one less card after dealing')

if __name__ == '__main__':
    unittest.main()