"""
Rock-Paper-Scissors : Game Logic Module
---------------------------------------
This module handles:
- Single round execution
- Random computer move
- Determining round results
- Playing a fixed 5-round match
"""

import random

MOVES = ["rock", "paper", "scissor"]

def get_computer_choice():
    # Return a random move for computer.
    return random.choice(MOVES)


def get_player_choice():

    for i, move in enumerate(MOVES):
        print(f"{i+1}. {move}")

    while True:
        
        u_move = input('Enter a choice (1-3): ')

        if u_move in ['1', '2', '3']:

            u_move = int(u_move) - 1
            player_choice = MOVES[u_move]
            break

        else:
            print("Sorry! That's not a valid choice.")

    return player_choice

def determine_round_result(player, computer):

    if player == computer:
        return "Tie"

    if (player == "rock"    and computer == "scissor") or \
       (player == "paper"   and computer == "rock")    or \
       (player == "scissor"  and computer == "paper"):
        
        return "Win"
    
    else:
        return "Lose"


def play_round():

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {player_choice} and Computer chose: {computer_choice}")
    result = determine_round_result(player_choice, computer_choice)
    return result


def play_match():

    player_score = 0
    computer_score = 0

    for round_no in range(1, 6):

        print(f"\nRound {round_no}\n")
        result = play_round()

        if result == "Win":
            print("You won")
            player_score += 5

        elif result == "Lose":
            print("You lose")
            computer_score += 5

        else:
            print("Round draw")

    if player_score > computer_score:
        match_result = "WIN"

    elif player_score < computer_score:
        match_result = "LOSE"
    
    else: 
        match_result = "DRAW"

    return player_score, computer_score, match_result