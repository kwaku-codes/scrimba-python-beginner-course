# Challenge: Update the Excuse Generator to accept user input.

# Right now all the variables are hardcoded. Let's fix that.
# 1. Replace each variable's value with an input() prompt.
# 2. Print and test — make sure your output still looks like this:
#    "Sorry [Ted], I can't go to [the movies] — I have [345] [bees] to [crochet]
#     and honestly it's taking longer than expected."

print(f"Welcome to the Excuse Generator! Please aanswer the following questions? ")

name = input("Who is the excuse for? ")
event = input("What is the event you are trying to avoid? ")
number = input("Give me a random number? ") 
noun = input("Give me a random noun? ")
verb = input ("Give me a verb? ")

excuse = f"Sorry {name}, I can't go to {event} — I have {number} {noun} to {verb} and honestly it's taking longer than expected."

print(excuse)