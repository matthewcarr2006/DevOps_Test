# Rock, Paper, Sissors game

import random
import time


def play_round(player1):
    
    rps_options = ["rock", "paper", "scissors"]
    computer = random.choice(rps_options) 

    if computer == player1:
        return "Draw. Let's go again."
    elif (computer == "rock" and player1 == "paper") or (computer == "paper" and player1 == "scissor") or computer == "scissors" and player1 == "rock":
        return "Player"
    else:
        return "Computer"
    

#def keep_score():
#    print("")
#    num_of_rounds = 0
#    user_wins = 0
#    computer_wins = 0
#    draws = 0



num_of_rounds = 0

rps_options = ["rock", "paper", "scissors"]

play_again = True

while play_again == True:

    if num_of_rounds == 0:
        play = input("Do you want to play Rock. Paper, Scissors? (Y/N): ")
    else: 
        time.sleep(3)
        play = input("Do you want to play again? (Y/N): ")

    if play.lower() == 'n':
        print("No problem, see you soon!")
        break


    player1_choice = input(f"Select rock, paper or scissors: ")
    if player1_choice.lower() == "x":
        print("See you later, quitter!")
        break
    elif player1_choice.lower() not in rps_options:
        print(f"In valid choice. Please try again or select 'x' to exit.")
    else:
        winner = play_round(player1_choice)
        if winner == 'player1':
            print("You've won!")
        else: print("computer wins")

    num_of_rounds += 1
    time.sleep(1)
    print(f"Number of rounds played: {num_of_rounds}")
    

    
        



