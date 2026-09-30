import random

board = [" "] * 9

def show_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


def check_winner():
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


while True:

    show_board()

    # Player's turn
    position = int(input("Enter position (1-9): ")) - 1

    if board[position] != " ":
        print("Position already taken!")
        continue

    board[position] = "X"

    # Check if player wins
    if check_winner() == "X":
        show_board()
        print("You win!")
        break

    # Check draw
    if " " not in board:
        show_board()
        print("Draw!")
        break

    # AI's turn
    empty = []

    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    ai_position = random.choice(empty)
    board[ai_position] = "O"

    print("AI chose position:", ai_position + 1)

    # Check if AI wins
    if check_winner() == "O":
        show_board()
        print("You lose!")
        break

    # Check draw
    if " " not in board:
        show_board()
        print("Draw!")
        break