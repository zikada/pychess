#!/usr/bin/env python3


def parse_line(x, board_state):
    line = "|"
    for i in board_state[x]:
        line = line + i + "|"
    return line


def parse_board(board_state):
    board = "+-+-+-+-+-+-+-+-+"
    for d, c in range(8):
        board = board + "\n" + str(c + 1) + " " + parse_line(d, board_state)
        board = board + "\n+-+-+-+-+-+-+-+-+"
    board = board + "\n\n   A B C D E F G H"
    return board


def action_validate(action):
    class InvalidAction(Exception):
        pass


def computer_move(board_state):
    pass
