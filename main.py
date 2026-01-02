# start building rock, paper, scissors game v2.0

# importing modules
from game import *
from scores import *

# greeting message for user
print("\nWelcome to Rock, Paper and Scissors Game v2.0!")

# helper function for pauses between actions
def pause():
    input('Press Enter to return')

# general information about the game
def rules_info():
    
    print("\n---------- Rules ----------\n")
    print('''In this game, you can play Rock-Paper-Scissors against computer.

➤ How Wins Are Decided:
   • Rock    beats Scissor
   • Scissor beats Paper
   • Paper   beats Rock
   • Same moves = Tie

➤ Match Format (v2.0):
   - A match consists of 5 fixed rounds
   - Final winner is decided after all 5 rounds

➤ Score System:
   +5 point if you win a round
   0 points for a tie
   +5 point to computer if it wins

Scores are saved in a text file, and you can view the score using in-game command.''')

# title screen of the application
def title_screen():

    print("\n------- Rock Paper Scissors -------\n")
    print("1. Start the game")
    print("2. View the scores")
    print("3. Rules and Information")
    print("4. Exit")
    print("\n-----------------------------------")

# main function of the application
def main():

    load_scores()           # loads the score

    while True:

        title_screen()          # display the title screen
        while True:

            choice = input("\nWhat do you want to do (1-4)? ")

            if choice == '1':
                print("\nStarting the game >>>\n")
                player_score, computer_score, match_result = play_match()
                update_lists(player_score, computer_score, match_result)

                pause()
                break

            elif choice == '2':
                view_scores()
                pause()
                break
            
            elif choice == '3':
                rules_info()
                pause()
                break

            elif choice == '4':
                print("Exiting the application..")
                return

            else:
                print("Sorry! That's not a valid choice. Try again ;)")


if __name__ == '__main__':
    main()

print("\nThanks for using our application!")