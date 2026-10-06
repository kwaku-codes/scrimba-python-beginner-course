# Challenge: Turn Order
# You're building a feature for a board game app that sets up each match.
# At the start of a game, you need to put the players in a random turn
# order, and also randomly choose one player to deal the cards.

# 1. Shuffle the players into a random turn order, then print the list.
# 2. Randomly choose one player to be the dealer and print:
#    "<name> deals first"

import random

players = ["Mara", "Devon", "Priya", "Leo"]

player_order = players

random.shuffle(players)
print(f"Player order for round one {player_order}")

card_dealer = random.choice(players)


print(f"{card_dealer} deals first")
