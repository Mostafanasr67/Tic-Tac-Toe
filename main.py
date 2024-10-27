from Functions import *
import keyboard
import time

art = r""" 
  _   _      _             _             
 | | (_)    | |           | |            
 | |_ _  ___| |_ __ _  ___| |_ ___   ___ 
 | __| |/ __| __/ _` |/ __| __/ _ \ / _ \
 | |_| | (__| || (_| | (__| || (_) |  __/
  \__|_|\___|\__\__,_|\___|\__\___/ \___|
"""

tokens = ['X', 'O']
turn = 1

def play(turn):
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    clear_screen()
    display_board(board, art)

    player1_win_status = False
    player2_win_status = False

    while True:
        while not player1_win_status and not player2_win_status:
            if turn == 1:
                token = tokens[1 - turn]
                player_no = 1
            else:
                token = tokens[turn * -1]
                player_no = 2

            if turn == 1:
                chosen_place = int(input(f"Player {player_no}, Choose your next move! (1-9): "))

                while chosen_place > 9 or chosen_place < 1:
                    chosen_place = int(input("Please choose a number from 1-9!: "))

                while board[chosen_place - 1] != ' ':
                    chosen_place = int(input("This place is already taken, please choose another one!: "))

                board[chosen_place - 1] = token
            else:
                print(board)
                chosen_place = find_winning_position(board)
                board[chosen_place] = token

            clear_screen()
            display_board(board, art)

            player1_win_status = check_win_p1(board)
            player2_win_status = check_win_p2(board)

            if player1_win_status:
                print("Congrats, Player 1 WON!")
                break

            if player2_win_status:
                print("Congrats, Player 2 WON!")
                break

            if all(element in ['X', 'O'] for element in board):
                print("It's a DRAW")
                break

            turn *= -1

        # Wait for either "R" to restart or "Esc" to exit
        print("To Play Again, Press 'R'. Press 'Esc' to exit.")
        while True:
            if keyboard.is_pressed('r'):
                time.sleep(0.2)  # Small delay to prevent multiple triggers
                play(turn=1)
                return
            elif keyboard.is_pressed('esc'):
                return

play(turn)