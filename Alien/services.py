from copy import deepcopy

from alien.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self._repo = repo
        self._coordinates = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6
        }

    def get_board(self):
        """
        :return: the board
        """
        return self._repo.board

    def get_aliens_remaining(self):
        """
        :return: the number of aliens remaining
        """
        return self._repo.aliens_remaining

    def get_board_without_aliens(self):
        """
        :return: the board without the aliens
        """
        board = deepcopy(self._repo.board)
        for i in range(7):
            for j in range(7):
                if board[i][j] == "X":
                    board[i][j] = ""
        return board

    def transform_coordinates(self, coord):
        """
        transforms the coordinates to the position in the matrix
        :param coord: the coordinates
        :return: the position in the matrix
        """
        letter = coord[0]
        number = int(coord[1])
        return self._coordinates[letter], number - 1

    def check_win(self):
        """
        :return: True if the player won, False otherwise
        """
        return self._repo.aliens_remaining == 0


    def move_aliens(self, fire_x, fire_y):
        """
        Moves the aliens
        Marks the aliens as destroyed if they are hit
        :param fire_x: The x coordinate of the fire
        :param fire_y: The y coordinate of the fire
        :return: True, if the aliens did not win yet, False otherwise
        """
        return self._repo.move_aliens(fire_x, fire_y)

