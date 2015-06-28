#!/usr/bin/env python3

import pychess

print("Welcome to PyChess! This is a CLI-based chess game using the Stockfish engine.")
input("Press Enter to continue... ")
boardState = ["RKTQMTKR", "        ", "        ", "        ", "        ", "        ", "        ", "RKTQMTKR"]
print("")
print(pychess.parse_board(boardState))
