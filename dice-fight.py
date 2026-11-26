import random

def roll_dice():
  roll = random.randint(1, 6)
  print(f"You rolled a {roll}!")

def throw_dice():
  roll_dice()
  roll_dice()

def show_welcome():
  print()
  print("Welcome to Dice Fight!")
  print()

def play_game():
  show_welcome()
  throw_dice()

play_game()