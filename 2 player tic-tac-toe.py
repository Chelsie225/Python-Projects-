#   Program Name:   tic-tac-toe.py
#
#   Author:         Adapted from code provided
#                   By Abhishek Sharma / January 26, 2023
#
#   Web Address:    www.machinelearningprojects.net/tic-tac-toe-game-in-python/
#
#   Date:           04/24/2023
#
#   Description:
#   This is a simple Tic-Tac-Toe game for two players written in Python.
#
# Tic-Tac-Toe game in Python


# Initialize Board to all blanks
board = [" " for x in range(9)]

# Print out board with values
def print_board():
    row1 = "  {} | {} | {} ".format(board[0], board[1], board[2])
    row2 = "  {} | {} | {} ".format(board[3], board[4], board[5])
    row3 = "  {} | {} | {} ".format(board[6], board[7], board[8])
    rowm = "-------------"

    print()
    print(row1)
    print(rowm)
    print(row2)
    print(rowm)
    print(row3)
    print()

def player_move(icon):

    # accept player's entry (verify they didn't select a used space)
    done = False    
    while done == False:    #   repeat until non-empty spot is selected.
        print("Your turn player ",icon)

        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon
            done = True
        else:
            print()
            print("That space is taken! TRY AGAIN!")

# determine if the player has won
def is_victory(icon):
    #   Evaluate all the rows to see if there is a winner
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon):
        return True
    #   Evaluate all the columns to see if there is a winner
    elif(board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon):
        return True
    #   Evaluate all the diagonals to see if there is a winner
    elif(board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
    #   No winner
        return False
    
# determine if the game is a draw
def is_draw():
    if " " not in board:
        return True
    else:
        return False


# main processing loop of game
print_board()
done=False
while done == False:
    for icon in ("X","O"):
        player_move(icon)
        print_board()
        if is_victory(icon):
            print(icon," wins! Congratulations!")
            done=True
            break
        elif is_draw():
            print("It's a draw!")
            done=True
            break
   
