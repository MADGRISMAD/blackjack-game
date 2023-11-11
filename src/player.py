class Player:
    def __init__(self, is_dealer=False):
        self.hand = []
        self.is_dealer = is_dealer

    def draw_card(self, deck):
        card = deck.deal()
        self.hand.append(card)

    def calculate_score(self):
        ace = False
        score = 0
        for card in self.hand:
            if card.value.isnumeric():
                score += int(card.value)
            elif card.value in ['J', 'Q', 'K']:
                score += 10
            elif card.value == 'A':
                ace = True
                score += 11
        if score > 21 and ace:
            score -= 10
        return score

    def display_hand(self):
        if self.is_dealer:
            print("Dealer's Hand:")
            print("Hidden")
            print(self.hand[1])
        else:
            print("Your Hand:")
            for card in self.hand:
                print(card)