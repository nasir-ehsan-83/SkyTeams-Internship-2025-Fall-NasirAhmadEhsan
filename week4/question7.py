import random

def rock_paper_scissors(player_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "Player wins"
    else:
        return "Computer wins"
