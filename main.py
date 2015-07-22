#!/usr/bin/env python3

import sys

import pychess

print("Welcome to PyChess, a CLI-based chess game using the Stockfish chess engine.")
input("Press Enter to continue...")
while True:
    try:
        white_or_black = str(input("Do you wanna play as white or black? "))
        if white_or_black != "white" and white_or_black != "black":
            raise Exception('The answer can only be "white" or "black"')
    except:
        print("Invalid answer.")
    else:
        if white_or_black == "white":
            board_state = [["r", "k", "t", "q", "m", "t", "k", "r"], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], ["R", "K", "T", "Q", "M", "T", "K", "R"]]
        else:
            board_state = [["R", "K", "T", "Q", "M", "T", "K", "R"], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], ["r", "k", "t", "q", "m", "t", "k", "r"]]
        break
while True:
    try:
        print("\n" + pychess.parse_board(board_state))
        action = str(input('Your move (type "quit" or "exit" to quit): '))
        if action == "quit" or action == "exit":
            sys.exit(0)
        else:
            pychess.action_validate(action)
    except SystemExit:
        raise
    except:
        print("Invalid action.")
    else:
        print("Thinking...")
        board_state = pychess.computer_move(board_state)
