from copy import deepcopy

from stellar_journey.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self._repo = repo

    def get_board(self):
        """
        :return: the board
        """
        return self._repo.board

    def get_row_E(self):
        """
        :return: the row where the Endevor ship is placed
        """
        return self._repo.row_E

    def get_col_E(self):
        """
        :return: the column where the Endevor ship is placed
        """
        return self._repo.col_E

    def change_E_coord(self, new_row, new_col):
        """
        Changes the position of the Endevor ship
        :param new_row: the new row
        :param new_col: the new column
        :return: the new board with the position changed successfully
        """
        self._repo.change_E_coord(new_row, new_col)

    def check_win(self):
        """
        Checks if the player has won
        :return: True = if the player has won, False = otherwise
        """
        for i in range(8):
            for j in range(8):
                if self._repo.board[i][j] == "B":
                    return False
        return True

    def board_with_adjacent_cruisers(self):
        """
        Creates a new board with the adjacent cruisers
        :return: the new board
        """
        new_table = deepcopy(self._repo.board)

        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for i in range(8):
            for j in range(8):
                if new_table[i][j] == "B":
                    k = 0

                    for (di, dj) in dirs:
                        if not self._repo.is_in_board(i + di, j + dj):
                            continue
                        if self._repo.board[i + di][j + dj] == "E":
                            k = 1
                    if k == 0:
                        new_table[i][j] = ""
        return new_table

    def adjacent_coordinates(self):
        """
        :return: the adjacent coordinates of the Endevor ship
        """
        row = self.get_row_E()
        col = self.get_col_E()
        adj_coords = []
        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for (di, dj) in dirs:
            if not self._repo.is_in_board(row + di, col + dj):
                continue
            adj_coords.append((row + di, col + dj))
        return adj_coords

    def transform_coordinates(self, coord):
        """
        transforms the coordinates to the position in the matrix
        :param coord: the coordinates
        :return: the position in the matrix
        """
        letter = coord[0]
        number = int(coord[1])
        if letter == "A":
            return 0, number - 1
        elif letter == "B":
            return 1, number - 1
        elif letter == "C":
            return 2, number - 1
        elif letter == "D":
            return 3, number - 1
        elif letter == "E":
            return 4, number - 1
        elif letter == "F":
            return 5, number - 1
        elif letter == "G":
            return 6, number - 1
        elif letter == "H":
            return 7, number - 1

    def place_random_cruisers(self, n):
        """
        Places the Blingon cruisers on the board
        :param n: the number of cruisers
        """
        self._repo.place_Blingon_cruisers(n)
