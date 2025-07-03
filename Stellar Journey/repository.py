import random


class Repo:
    def __init__(self):
        self._board = [["" for _ in range(8)] for _ in range(8)]
        self.place_random_stars()
        self._row_E, self._col_E = self.place_Endevor_ship()
        self.place_Blingon_cruisers(3)

    @property
    def board(self):
        return self._board

    @property
    def row_E(self):
        return self._row_E

    @property
    def col_E(self):
        return self._col_E

    def is_in_board(self, row, col):
        """
        check if x[row][col] is on board
        :param row: the row in the board
        :param col: the col in the board
        :return: True = its in the board, False = otherwise
        """
        return 0 <= row < 8 and -1 < col <= 7

    def place_random_stars(self):
        """
        Places 10 random adjacent stars
        :return: the new board
        """
        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for _ in range(10):
            generated = False
            while not generated:
                row = random.randint(0, 7)
                col = random.randint(0, 7)
                valid = True

                for (di, dj) in dirs:
                    new_row = row + di
                    new_col = col + dj
                    if not self.is_in_board(new_row, new_col):
                        continue
                    if self._board[new_row][new_col] != "":
                        valid = False
                        break

                if valid:
                    self._board[row][col] = "*"
                    generated = True

    def place_Endevor_ship(self):
        """
        Places the players ship on the board
        :return: the new board
        """
        while True:
            row = random.randint(0, 7)
            col = random.randint(0, 7)
            if self._board[row][col] != "*":
                self._board[row][col] = "E"
                break
        return row, col

    def place_Blingon_cruisers(self, n):
        """
        Places the Blingon cruisers on the board
        :param n: the number of cruisers
        :return: the new board
        """

        for i in range(8):
            for j in range(8):
                if self._board[i][j] == "B":
                    self._board[i][j] = ""

        for _ in range(n):
            while True:
                row = random.randint(0, 7)
                col = random.randint(0, 7)
                if self._board[row][col] != "*" and self._board[row][col] != "E" and self._board[row][col] != "B":
                    self._board[row][col] = "B"
                    break

    def change_E_coord(self, new_row, new_col):
        """
        Changes the position of the Endevor ship
        :param new_row: the new row
        :param new_col: the new column
        :return: the new board with the position changed successfully
        """
        self._board[self._row_E][self.col_E] = ""
        self._board[new_row][new_col] = "E"
        self._row_E = new_row
        self._col_E = new_col
