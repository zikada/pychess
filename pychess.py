#!/usr/bin/env python3


def parse_line(x, board_state):
    line = "|"
    for i in board_state[x]:
        line += i + "|"
    return line


def parse_board(board_state):
    board = "   +-+-+-+-+-+-+-+-+ "
    for d in range(8):
        c = range(8, 0, -1)
        board += "\n " + str(c[d]) + " " + parse_line(d, board_state) + " "
        board += "\n   +-+-+-+-+-+-+-+-+ "
    board += "\n\n    A B C D E F G H  "
    return board

# def action_validate(action):
#     class InvalidAction(Exception):
#         pass
#
#
# Buggy function: It looks like the pass statement makes the board_state variable become None (null)
# def computer_move(board_state):
#     pass
