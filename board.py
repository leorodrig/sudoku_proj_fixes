"""
for the purposes of this, we will ignore all the functionality
relating to pygame and only include a terminal representation of
the program.
"""

from cell import Cell
from sudoku_generator import SudokuGenerator
import colorama
colorama.init()
# colorama will be used to display sketched values in this version


class Board:
    red = colorama.Fore.RED
    red_reset = colorama.Fore.RESET
    row_UI = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, difficulty):
        # will not include height width and screen for this version
        self.difficulty = difficulty
        if difficulty == "e":
            removed_cells = 30
        elif difficulty == "m":
            removed_cells = 40
        else:
            removed_cells = 50
        twod_board = SudokuGenerator(9, removed_cells)
        twod_board.fill_diagonal()
        self.original_board = twod_board.original_board
        self.editable_board = []
        for row in range(9):
            self.editable_board.append([])
            for col in range(9):
                self.editable_board[row].append(Cell(twod_board.original_board[row][col], row, col))
        # attributes relating to cell
        self.current_cell = None

    def draw(self):
        # prints out the board
        for num in range(9):
            self.editable_board[num].insert(0, f"{board.red} {num + 1} {board.red_reset}")
        print(self.red + "   1 2 3 4 5 6 7 8 9" + board.red_reset, end="")
        for i in range(9):
            print()
            for j in range(10):
                if type(self.editable_board[i][j]) is str:
                    print(self.editable_board[i][j], end="")
                else:
                    self.editable_board[i][j].draw()

    def select(self, row, col):
        self.current_cell = self.editable_board[row][col + 1]

    def clear(self, row, col): # row and col essentially replace click and select
        if self.original_board[row][col] == 0:
            self.current_cell.set_cell_value(0)
        else:
            pass

    def sketch(self, value):
        self.current_cell.set_sketched_value = value

    def place_number(self, value):
        self.current_cell = value

    def reset_to_original(self):
        # this function will basically just recall the function used to initialize board
        self.editable_board = []
        for row in range(9):
            self.editable_board.append([])
            for col in range(9):
                self.editable_board[row].append(Cell(self.original_board[row][col], row, col))

    # def is_full(self):
    #     for row in range(9):
    #         for cell in range(9):
    #             if



# board = Board("e")
# for num in range(9):
#     board.board[num].insert(0, f"{board.red} {num + 1} {board.red_reset}")
# print(board.red + "   1 2 3 4 5 6 7 8 9" + board.red_reset, end="")
# for i in range(9):
#     print()
#     for j in range(10):
#         if type(board.board[i][j]) is str:
#             print(board.board[i][j], end="")
#         else:
#             board.board[i][j].draw()


board = Board("e")
board.draw()
