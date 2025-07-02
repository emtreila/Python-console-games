from game_of_life.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self._repo = repo

    def get_pattern(self, pattern):
        """
        gets the pattern from the repository
        :param pattern: the pattern to get
        :return: the matrix with the pattern
        """
        self._repo.set_file_name(pattern)
        return self._repo.read_from_file()

    def place_pattern(self, pattern, x, y, table):
        """
        places the pattern on the board
        :param pattern: the pattern to place
        :param x: the x coordinate
        :param y: the y coordinate
        :param table: the game table
        :return: the game table, updated
        """
        for i in range(len(pattern)):
            for j in range(len(pattern[i])):
                x_i = x + i
                y_j = y + j

                if x_i < 0 or x_i > 7 or y_j < 0 or y_j > 7:
                    continue

                table[x_i][y_j] = pattern[i][j]

    def tick(self, table):
        """
        makes a tick
        :param table: the game table
        :return: the game table, updated
        """

        new_table = [['_' for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                if table[i][j] == "_":
                    if self.get_neighbours(i, j, table) == 3:
                        new_table[i][j] = "x"
                    else:
                        new_table[i][j] = "_"
                else:
                    n = self.get_neighbours(i, j, table)
                    if n < 2 or n > 3:
                        new_table[i][j] = "_"
                    else:
                        new_table[i][j] = "x"
        return new_table

    def get_neighbours(self, x_cell, y_cell, table):
        """
        gets the number of alive neighbours of the cell
        :param x_cell: the x coordinate of the cell
        :param y_cell: the y coordinate of the cell
        :param table: the table
        :return: number of alive neighbours
        """
        n = 0
        if self.check_index(x_cell + 1) and self.check_index(y_cell + 1) and table[x_cell + 1][y_cell + 1] == "x":
            n += 1
        if self.check_index(x_cell - 1) and self.check_index(y_cell - 1) and table[x_cell - 1][y_cell - 1] == "x":
            n += 1
        if self.check_index(x_cell + 1) and self.check_index(y_cell - 1) and table[x_cell + 1][y_cell - 1] == "x":
            n += 1
        if self.check_index(x_cell - 1) and self.check_index(y_cell + 1) and table[x_cell - 1][y_cell + 1] == "x":
            n += 1
        if self.check_index(x_cell + 1) and table[x_cell + 1][y_cell] == "x":
            n += 1
        if self.check_index(x_cell - 1) and table[x_cell - 1][y_cell] == "x":
            n += 1
        if self.check_index(y_cell + 1) and table[x_cell][y_cell + 1] == "x":
            n += 1
        if self.check_index(y_cell - 1) and table[x_cell][y_cell - 1] == "x":
            n += 1
        return n

    def check_index(self, index):
        """
        checks if the index is valid
        :param index: the index
        :return: True if the index is valid, False otherwise
        """
        return 0 <= index < 8

    def save_to_file(self, table):
        """
        saves the current table to a file
        :param table: the table to save
        """
        self._repo.save_to_file(table)

    def load_from_file(self):
        """
        loads the table from a file
        :return: the table
        """
        return self._repo.load_from_file()
