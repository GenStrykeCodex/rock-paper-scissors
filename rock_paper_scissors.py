import random

def score(comp_win: int, user_win: int):    # Calculate scores based on wins
    c_score = comp_win * 5
    u_score = user_win * 5
    scores = (u_score, c_score)
    return scores

def game_winner(u_score: int, c_score: int):    # Determine the overall winner

    if c_score > u_score:
        print("The computer won the game.")

    elif c_score < u_score:
        print("You won the game.")

    else:
        print("It is a tie.")


def play_round(u_win, c_win):   # Play a single round of the game

    move = input("Rock, Paper or Scissor: ")
    move = move.lower()  # Normalize input to lowercase

    if move == "rock" or move == "paper" or move == "scissor":
        c = random.randint(1, 3)

        if c == 1:
            c_move = "rock"

        elif c == 2:
            c_move = "paper"

        else:
            c_move = "scissor"

    else:
        print("The input is invalid. Try again.")
        return play_round(u_win, c_win) #return the function.
    
    print(f"The computer chose {c_move}")

    # Determine the outcome of the round

    if move == c_move:
        print("Draw")

    else:
        if move == "rock": 

            if c_move == "paper":
                print("You lose.")
                c_win += 1

            else:
                print("You win.")
                u_win += 1

        elif move == "paper":

            if c_move == "scissor":
                print("You lose.")
                c_win += 1

            else:
                print("You win.")
                u_win += 1

        elif move == "scissor":

            if c_move == "rock":
                print("You lose.")
                c_win += 1

            else:
                print("You win.")
                u_win += 1

        else:
            print("Invalid move. Please enter Rock, Paper, or Scissor.")

    return u_win, c_win

def game(): # Main function to run the game
    
    u_win = 0
    c_win = 0

    while True:
        u_win, c_win = play_round(u_win, c_win)
        again = input("Do you want to play again? ")

        if again == "Yes" or again == "yes":
            continue

        elif again == "No" or again == 'no':
            print(f"Your win: {u_win}  Computer's win: {c_win}")
            a, b = score(c_win, u_win)
            print(f"Your score: {a}  Computer's score: {b}")
            game_winner(a, b)
            break

        else:
            print("Answer in yes or no.")

game()
print("GAME ENDED")