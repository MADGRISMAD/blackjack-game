import random
from player import Player
from card import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player(False)
        self.dealer = Player(True)

    def start_game(self):
        self.deck.shuffle()

        self.player.draw_card(self.deck)
        self.player.draw_card(self.deck)
        self.dealer.draw_card(self.deck)
        self.dealer.draw_card(self.deck)

        print("Welcome to Blackjack!")
        print("Your hand:", self.player.display_hand())
        print("Dealer's hand: [{}][?]".format(self.dealer.hand[0]))

    def deal_cards(self):
        while self.player.calculate_score() < 21:
            choice = input("Do you want to hit or stand? ")
            if choice.lower() == "hit":
                self.player.draw_card(self.deck)
                print("Your hand:", self.player.display_hand())
            elif choice.lower() == "stand":
                break
            else:
                print("Invalid choice. Please choose to hit or stand.")

        while self.dealer.calculate_score() < 17:
            self.dealer.draw_card(self.deck)

    def check_blackjack(self):
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        if player_score == 21 and dealer_score != 21:
            print("Blackjack! You win!")
            return True
        elif dealer_score == 21 and player_score != 21:
            print("Dealer got a blackjack. You lose.")
            return True
        elif player_score == 21 and dealer_score == 21:
            print("Both you and the dealer got a blackjack. It's a tie.")
            return True

        return False

    def end_game(self):
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        print("Your hand:", self.player.display_hand())
        print("Dealer's hand:", self.dealer.display_hand())

        if player_score > 21:
            print("You busted. You lose.")
        elif dealer_score > 21:
            print("Dealer busted. You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score < dealer_score:
            print("You lose.")
        else:
            print("It's a tie.")