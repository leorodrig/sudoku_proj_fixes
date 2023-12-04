"""
for the purposes of this, we will ignore all the functionality
relating to pygame and only include a terminal representation of
the program.
"""

from cell import Cell
import colorama
colorama.init()
# colorama will be used to display sketched values in this version


class Board:
    red = colorama.Fore.RED
    red_reset = colorama.Fore.RESET
    row_UI = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    col_UI = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, difficulty):
        # will not include height width and screen for this version
        # difficulty will be "e", "m", or "h"
        if difficulty == "e":
            self.difficulty = 30
        elif difficulty == "m":
            self.difficulty = 40
        elif difficulty == "h":
            self.difficulty = 50

    def draw(self):
        pass
        # not needed in this version since it is purely UI

    def select(self, row, col):
        pass

    def clear(self, row, col): # row and col essentially replace click and select
        # clears a spot on the board if its value was originally 0
        pass


