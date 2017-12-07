from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board_in):
    for row in board_in:
        print(" ".join(row))

print_board(board)

def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

turn = 0
for turn in range(4):

    print(" ")
    print("Turn", turn + 1)

    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break

    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")

        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")

        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)

            if turn == 3:
                print(" ")
                print("Game Over, the battleship was in "
                      + str(ship_row) + "x" + str(ship_col))

                board[ship_row][ship_col] = "*"
                print_board(board)

    left_turns = 3 - turn
    print("You have " + str(left_turns))