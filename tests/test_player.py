import unittest
from src.player import Player
from src.card import Card

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_draw_card(self):
        card = Card('Hearts', 'A')
        self.player.draw_card(card)
        self.assertEqual(self.player.hand[0], card)

    def test_calculate_score(self):
        cards = [Card('Hearts', 'A'), Card('Diamonds', '10')]
        for card in cards:
            self.player.draw_card(card)
        self.assertEqual(self.player.calculate_score(), 21)

    def test_display_hand(self):
        cards = [Card('Hearts', 'A'), Card('Diamonds', '10')]
        for card in cards:
            self.player.draw_card(card)
        self.assertEqual(self.player.display_hand(), 'A of Hearts, 10 of Diamonds')

if __name__ == '__main__':
    unittest.main()