#!/usr/bin/env python3

import sys

import pychess

print("Welcome to PyChess, a CLI-based chess game using the Stockfish chess engine.")
input("Press Enter to continue... ")
board_state = [["R", "K", "T", "Q", "M", "T", "K", "R"], [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "], ["R", "K", "T", "Q", "M", "T", "K", "R"]]
try:
    print("\n" + pychess.parse_board(board_state))
    action = str(input("Your move (type \"quit\" or \"exit\" to quit): "))
    if ("quit" or "exit") in action:
        sys.exit(0)
    pychess.action_validate(action)
except:
    print("Invalid action.")
else:
    print("Thinking...")
    board_state = pychess.computer_move(board_state)
