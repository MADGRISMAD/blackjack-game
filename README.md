# Blackjack Game

This is a simple command line Blackjack game implemented in Python.

## Project Structure

The project has the following structure:

```
blackjack-game
├── src
│   ├── main.py
│   ├── game.py
│   ├── player.py
│   └── card.py
├── tests
│   ├── test_game.py
│   ├── test_player.py
│   └── test_card.py
├── .gitignore
├── requirements.txt
└── README.md
```

## How to Run

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the game:

```bash
python src/main.py
```

## Game Rules

The game is a simplified version of Blackjack (21). The rules are as follows:

- The game is played with a deck of 52 cards.
- The goal of the game is to get as close to 21 as possible, without going over.
- Each player starts with two cards. One of the dealer's cards is hidden until the end.
- Players can choose to 'Hit' to take another card, or 'Stand' to stop taking cards.
- If a player's hand exceeds 21, they bust and lose the game.
- If a player hits Blackjack (21 with their first two cards), they win.
- If the dealer busts, all remaining players win.
- If no one busts, the player with the highest hand wins. If there's a tie, the dealer wins.

## Classes

- `Game`: This class handles the game logic.
- `Player`: This class represents a player. Each player has a hand of cards and can be a dealer.
- `Card`: This class represents a card. Each card has a suit and a value.
- `Deck`: This class represents a deck of cards.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)