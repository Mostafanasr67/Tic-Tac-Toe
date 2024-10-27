import os
import random


def display_board(board, art):
    print(art)

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win_p1(board):
    # Check Rows
    for i in range(0, 9, 3):  # Check every 3 elements (rows)
        if board[i] == board[i + 1] == board[i + 2] == "X":
            return True

    # Check Columns
    for i in range(3):  # Check each column
        if board[i] == board[i + 3] == board[i + 6] == "X":
            return True

    # Check Diagonals
    if board[0] == board[4] == board[8] == "X":
        return True
    if board[2] == board[4] == board[6] == "X":
        return True

    return False  # Return False if no win condition is met



def check_win_p2(board):
    # Check Rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == "O":
            return True

    # Check Columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == "O":
            return True

    # Check Diagonals
    if board[0] == board[4] == board[8] == "O":
        return True
    if board[2] == board[4] == board[6] == "O":
        return True

    return False


def clear_screen():
    print("\n" * 100)  # Prints 100 newlines

def p2_choice(board):
    flag = True

    while flag:
        position = random.randint(0, 8)
        if board[position] == ' ':
            return position


def find_winning_position(board):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == 'O' and board[c] == ' ':
            return c
        if board[a] == board[c] == 'O' and board[b] == ' ':
            return b
        if board[b] == board[c] == 'O' and board[a] == ' ':
            return a

    for a, b, c in winning_combinations:
        if board[a] == board[b] == 'X' and board[c] == ' ':
            return c
        if board[a] == board[c] == 'X' and board[b] == ' ':
            return b
        if board[b] == board[c] == 'X' and board[a] == ' ':
            return a

    return p2_choice(board)


