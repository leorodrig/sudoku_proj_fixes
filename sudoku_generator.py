import random


class SudokuGenerator:

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length  # will always = 9
        self.removed_cells = removed_cells
        self.box_length = row_length / 3
        self.original_board = []

    def get_board(self):
        return self.original_board

    def print_board(self):
        pass

    def valid_in_row(self, row, num):
        # for i in range(0, 9):
        #     if self
        pass

    def valid_in_col(self, col, num):
        pass

    def valid_in_box(self, row_start, col_start, num):
        pass

    def is_valid(self, row, col, num):
        # if self.original_board[row][col] == 0 and self.original_board[row][col] != num:
        #     return True
        # else:
        #     return False
        # pass
        pass

    def fill_box(self, row_start, col_start):
        pass

    def fill_diagonal(self):
        # this will begin by initializing an empty board
        self.original_board = [[0 for _ in range(self.row_length)] for _ in range(self.row_length)]
        # now that we have an empty board, we will fill the top left
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(numbers_list)
        j = 0
        for row in range(3):
            for col in range(3):
                self.original_board[row][col] = numbers_list[j]
                j += 1
        # middle box
        random.shuffle(numbers_list)
        j = 0
        for row in range(3, 6):
            for col in range(3, 6):
                self.original_board[row][col] = numbers_list[j]
                j += 1
        # bottom right box
        random.shuffle(numbers_list)
        j = 0
        for row in range(6, 9):
            for col in range(6, 9):
                self.original_board[row][col] = numbers_list[j]
                j += 1
        return self.original_board

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.original_board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.original_board[row][col] = 0
        return False

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    def remove_cells(self):
        # generate all coordinates on the board
        all_coordinates = [(i, j) for i in range(9) for j in range(9)]
        # select number of coordinates


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
