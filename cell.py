class Cell:
    def __init__(self, value, row, col):
        # initializer for the cell
        # note: this version will not include the screen
        self.value = value
        self.row = row
        self.col = col
        self.sketched_value = None

    def set_cell_value(self, value):
        # sets cell value
        self.value = value

    def set_sketched_value(self, value):
        # sets the sketched value
        self.sketched_value = value

    def draw(self):
        # draws out the value
        if self.value != 0:
            print(self.value, end=" ")
        else:
            if self.sketched_value is not None:
                print(self.sketched_value, end=" ")
            else:
                print(0, end=" ")
