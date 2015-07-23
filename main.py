#!/usr/bin/env python3

import sys

import pychess

print("Welcome to PyChess, a CLI-based chess game using UCI-compatible chess engines.")
input("Press Enter to continue...")
while True:
    try:
        global white_or_black
        white_or_black = str(input("Do you wanna play as white or black? "))
        if white_or_black != "white" and white_or_black != "black":
            raise Exception('The answer can only be "white" or "black"')
    except:
        print("Invalid answer.")
    else:
        global board_state
        if white_or_black == "white":
            board_state = [["r", "k", "t", "q", "m", "t", "k", "r"], ["p", "p", "p", "p", "p", "p", "p", "p"],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           ["P", "P", "P", "P", "P", "P", "P", "P"], ["R", "K", "T", "Q", "M", "T", "K", "R"]]
        else:
            board_state = [["R", "K", "T", "Q", "M", "T", "K", "R"], ["P", "P", "P", "P", "P", "P", "P", "P"],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " ", " "],
                           ["p", "p", "p", "p", "p", "p", "p", "p"], ["r", "k", "t", "q", "m", "t", "k", "r"]]
        break
global squares
squares = {board_state[0][0]: "a8", board_state[0][1]: "b8", board_state[0][2]: "c8", board_state[0][3]: "d8",
           board_state[0][4]: "e8", board_state[0][5]: "f8", board_state[0][6]: "g8", board_state[0][7]: "h8",
           board_state[1][0]: "a7", board_state[1][1]: "b7", board_state[1][2]: "c7", board_state[1][3]: "d7",
           board_state[1][4]: "e7", board_state[1][5]: "f7", board_state[1][6]: "g7", board_state[1][7]: "h7",
           board_state[2][0]: "a6", board_state[2][1]: "b6", board_state[2][2]: "c6", board_state[2][3]: "d6",
           board_state[2][4]: "e6", board_state[2][5]: "f6", board_state[2][6]: "g6", board_state[2][7]: "h6",
           board_state[3][0]: "a5", board_state[3][1]: "b5", board_state[3][2]: "c5", board_state[3][3]: "d5",
           board_state[3][4]: "e5", board_state[3][5]: "f5", board_state[3][6]: "g5", board_state[3][7]: "h5",
           board_state[4][0]: "a4", board_state[4][1]: "b4", board_state[4][2]: "c4", board_state[4][3]: "d4",
           board_state[4][4]: "e4", board_state[4][5]: "f4", board_state[4][6]: "g4", board_state[4][7]: "h4",
           board_state[5][0]: "a3", board_state[5][1]: "b3", board_state[5][2]: "c3", board_state[5][3]: "d3",
           board_state[5][4]: "e3", board_state[5][5]: "f3", board_state[5][6]: "g3", board_state[5][7]: "h3",
           board_state[6][0]: "a2", board_state[6][1]: "b2", board_state[6][2]: "c2", board_state[6][3]: "d2",
           board_state[6][4]: "e2", board_state[6][5]: "f2", board_state[6][6]: "g2", board_state[6][7]: "h2",
           board_state[7][0]: "a1", board_state[7][1]: "b1", board_state[7][2]: "c1", board_state[7][3]: "d1",
           board_state[7][4]: "e1", board_state[7][5]: "f1", board_state[7][6]: "g1", board_state[7][7]: "h1"}
while True:
    try:
        if white_or_black == "white":
            print("\n" + pychess.parse_board(board_state) + "\n")
        else:
            print("\n" + pychess.parse_board(board_state)[::-1] + "\n")
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
