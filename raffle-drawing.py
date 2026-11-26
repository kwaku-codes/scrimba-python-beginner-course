# WHAT'S THIS THEN?
# This file covers how to use the While Loop with the "in" keyword to see what values 
# are already available in a list and if we can call them. The challenge below is 
# meant to help build on that understanding by creating a raffle game 
# ============================================================================
# import random

# pick = random.choice(bingo_numbers)

# while pick in already_called:
#   pick = random.choice(bingo_numbers)

# print(f"Next call: {pick}")
# already_called.append(pick)
# print(already_called)

# Challenge: Raffle Drawing
# Build a feature that manages a charity raffle. The program picks a random winner but
# makes sure nobody wins twice. If the random winner has already won a prize, keep 
# drawing a random winner until you land on someone new.
# 1. Draw a random name from entrants.
# 2. If that name is already in winners, keep drawing until you get one
#    that isn't.
# 3. Add the new winner to winners and print: "Winner: <name>"


entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
winners = ["Diego", "Sofia"]

import random

name = random.choice(entrants)
while name in winners: 
    name = random.choice(entrants)

winners.append(name)
print(f"Winner: {name}")
