import unittest
from src.game import Game
from src.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.player = Player(is_dealer=False)
        self.dealer = Player(is_dealer=True)

    def test_start_game(self):
        self.game.start_game(players=[self.player, self.dealer])
        self.assertEqual(len(self.player.hand), 2)
        self.assertEqual(len(self.dealer.hand), 2)

    def test_deal_cards(self):
        self.game.deal_cards(self.player, num=1)
        self.assertEqual(len(self.player.hand), 1)

    def test_check_blackjack(self):
        self.player.hand = [ ('Hearts', 10), ('Spades', 'A') ]
        self.assertTrue(self.game.check_blackjack(self.player))

    def test_end_game(self):
        self.player.hand = [ ('Hearts', 10), ('Spades', 'A') ]
        self.dealer.hand = [ ('Hearts', 9), ('Spades', 'A') ]
        winner = self.game.end_game(players=[self.player, self.dealer])
        self.assertEqual(winner, self.player)

if __name__ == '__main__':
    unittest.main()