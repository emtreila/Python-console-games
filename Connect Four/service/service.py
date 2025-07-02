import numpy as np

from repository.repository import MemoRepo


class Service:
    def __init__(self, board_repo: MemoRepo):
        self._board_repo = board_repo

    def print_board(self):
        """
        Returns the board flipped for playing Connect 4
        :return: the board
        """
        return np.flip(self._board_repo.board, 0)

    def is_valid_row(self, col, row):
        """
        Check if the row is ok
        :param col: the column
        :param row: the row to check
        :return: True if its ok
                False otherwise
        """

        if self._board_repo.board[col][row - 1] == 0:
            return False
        return True

    def is_valid_location(self, col):
        """
        Checks to see if we can add another piece to the column where the user moved a piece to
        :param col: the column where the piece is put
        :return: True if we can add another piece to that column
                 False if the column is full of pieces
        """
        if self._board_repo.board[5][col] == 0:
            return True
        return False

    def get_open_row(self, col):
        """
        Returns the position where the piece falls
        :param col: the column where the piece is put
        :return: the row where the piece is put
        """
        for row in range(6):
            if self._board_repo.board[row][col] == 0:
                return row

    def put_piece(self, row, col, piece):
        """
        Puts the piece on the board
        :param row: the row the piece is put on
        :param col: the column the piece is put on
        :param piece: the piece 1 = user   2 = computer
        """
        self._board_repo.put_piece(row, col, piece)

    def is_won(self, piece):
        """
        Check to see if the game is won
        :param piece: 1 = user   2 = computer
        :return: True = game won, False otherwise
        """

        # Check to see if we have 4 pieces in a row HORIZONTALLY
        for col in range(4):  # 4 because we cant have 4 in a row on position 4,5,6
            for row in range(6):
                if self._board_repo.board[row][col] == piece and self._board_repo.board[row][col + 1] == piece \
                        and self._board_repo.board[row][col + 2] == piece and \
                        self._board_repo.board[row][col + 3] == piece:
                    return True

        # Check to see if we have 4 pieces in a row VERTICALLY
        for col in range(7):
            for row in range(3):
                if self._board_repo.board[row][col] == piece and self._board_repo.board[row + 1][col] == piece \
                        and self._board_repo.board[row + 2][col] == piece and \
                        self._board_repo.board[row + 3][col] == piece:
                    return True

        # Check to see if we have 4 pieces in a row DIAGONALLY ( / and \ )
        for col in range(4):
            for row in range(3):
                if self._board_repo.board[row][col] == piece and self._board_repo.board[row + 1][col + 1] == piece \
                        and self._board_repo.board[row + 2][col + 2] == piece and \
                        self._board_repo.board[row + 3][col + 3] == piece:
                    return True

        for col in range(4):
            for row in range(3, 6):
                if self._board_repo.board[row][col] == piece and self._board_repo.board[row - 1][col + 1] == piece and \
                        self._board_repo.board[row - 2][col + 2] == piece and \
                        self._board_repo.board[row - 3][col + 3] == piece:
                    return True

    def is_tie(self):
        """
        Checks to see if there is a tie
        :return: True = tie, False otherwise
        """
        if self._board_repo.board[5][0] != 0 and self._board_repo.board[5][1] != 0 and self._board_repo.board[5][2] != 0 \
                and self._board_repo.board[5][3] != 0 and self._board_repo.board[5][4] != 0 and \
                self._board_repo.board[5][5] != 0 and self._board_repo.board[5][6] != 0:
            return True

    def winning_move_computer(self):
        """
        Checks to see if there are 3 pieces put by the computer such that he can win the game with the next move
        :return: the row and column for which the next move wins the game
        """
        # Check horizontally
        for col in range(4):  # 4 because we cant have 4 in a row on position 4,5,6
            for row in range(6):
                if self._board_repo.board[row][col] == 2 and self._board_repo.board[row][col + 1] == 2 and \
                        self._board_repo.board[row][col + 2] == 2 and \
                        self._board_repo.board[row][col + 3] == 0:
                    return row, col + 3
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row][col + 1] == 2 and \
                        self._board_repo.board[row][col + 2] == 0 and \
                        self._board_repo.board[row][col + 3] == 2:
                    return row, col + 2
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row][col + 1] == 0 and \
                        self._board_repo.board[row][col + 2] == 2 and \
                        self._board_repo.board[row][col + 3] == 2:
                    return row, col + 1

        # Check vertically
        for col in range(7):
            for row in range(3):
                if self._board_repo.board[row][col] == 2 and self._board_repo.board[row + 1][col] == 2 and \
                        self._board_repo.board[row + 2][col] == 2 and \
                        self._board_repo.board[row + 3][col] == 0:
                    return row + 3, col
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row + 1][col] == 2 and \
                        self._board_repo.board[row + 2][col] == 0 and \
                        self._board_repo.board[row + 3][col] == 2:
                    return row + 2, col
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row + 1][col] == 0 and \
                        self._board_repo.board[row + 2][col] == 2 and \
                        self._board_repo.board[row + 3][col] == 2:
                    return row + 1, col

        # Check diagonally ( / )
        for col in range(4):
            for row in range(3):
                if self._board_repo.board[row][col] == 2 and self._board_repo.board[row + 1][col + 1] == 2 and \
                        self._board_repo.board[row + 2][col + 2] == 2 and \
                        self._board_repo.board[row + 3][col + 3] == 0:
                    return row + 3, col + 3
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row + 1][col + 1] == 2 and \
                        self._board_repo.board[row + 2][col + 2] == 0 and \
                        self._board_repo.board[row + 3][col + 3] == 2:
                    return row + 2, col + 2
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row + 1][col + 1] == 0 and \
                        self._board_repo.board[row + 2][col + 2] == 2 and \
                        self._board_repo.board[row + 3][col + 3] == 2:
                    return row + 1, col + 1

        # Check diagonally ( \ )
        for col in range(4):
            for row in range(3, 6):
                if self._board_repo.board[row][col] == 2 and self._board_repo.board[row - 1][col + 1] == 2 and \
                        self._board_repo.board[row - 2][col + 2] == 2 and \
                        self._board_repo.board[row - 3][col + 3] == 0:
                    return row - 3, col + 3
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row - 1][col + 1] == 2 and \
                        self._board_repo.board[row - 2][col + 2] == 0 and \
                        self._board_repo.board[row - 3][col + 3] == 2:
                    return row - 2, col + 2
                elif self._board_repo.board[row][col] == 2 and self._board_repo.board[row - 1][col + 1] == 0 and \
                        self._board_repo.board[row - 2][col + 2] == 2 and \
                        self._board_repo.board[row - 3][col + 3] == 2:
                    return row - 1, col + 1

        return None

    def winning_move_user(self):
        """
        Checks to see if there are 3 pieces put by the user such that he can win the game with the next move
        :return: the row and column for which the next move wins the game
        """
        # Check horizontally
        for col in range(4):  # 4 because we cant have 4 in a row on position 4,5,6
            for row in range(6):
                if self._board_repo.board[row][col] == 1 and self._board_repo.board[row][col + 1] == 1 and \
                        self._board_repo.board[row][col + 2] == 1 and \
                        self._board_repo.board[row][col + 3] == 0:
                    return row, col + 3
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row][col + 1] == 1 and \
                        self._board_repo.board[row][col + 2] == 0 and \
                        self._board_repo.board[row][col + 3] == 1:
                    return row, col + 2
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row][col + 1] == 0 and \
                        self._board_repo.board[row][col + 2] == 1 and \
                        self._board_repo.board[row][col + 3] == 1:
                    return row, col + 1

        # Check vertically
        for col in range(7):
            for row in range(3):
                if self._board_repo.board[row][col] == 1 and self._board_repo.board[row + 1][col] == 1 and \
                        self._board_repo.board[row + 2][col] == 1 and \
                        self._board_repo.board[row + 3][col] == 0:
                    return row + 3, col
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row + 1][col] == 1 and \
                        self._board_repo.board[row + 2][col] == 0 and \
                        self._board_repo.board[row + 3][col] == 1:
                    return row + 2, col
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row + 1][col] == 0 and \
                        self._board_repo.board[row + 2][col] == 1 and \
                        self._board_repo.board[row + 3][col] == 1:
                    return row + 1, col

        # Check diagonally ( / )
        for col in range(4):
            for row in range(3):
                if self._board_repo.board[row][col] == 1 and self._board_repo.board[row + 1][col + 1] == 1 and \
                        self._board_repo.board[row + 2][col + 2] == 1 and \
                        self._board_repo.board[row + 3][col + 3] == 0:
                    return row + 3, col + 3
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row + 1][col + 1] == 1 and \
                        self._board_repo.board[row + 2][col + 2] == 0 and \
                        self._board_repo.board[row + 3][col + 3] == 1:
                    return row + 2, col + 2
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row + 1][col + 1] == 0 and \
                        self._board_repo.board[row + 2][col + 2] == 1 and \
                        self._board_repo.board[row + 3][col + 3] == 1:
                    return row + 1, col + 1

        # Check diagonally ( \ )
        for col in range(4):
            for row in range(3, 6):
                if self._board_repo.board[row][col] == 1 and self._board_repo.board[row - 1][col + 1] == 1 and \
                        self._board_repo.board[row - 2][col + 2] == 1 and \
                        self._board_repo.board[row - 3][col + 3] == 0:
                    return row - 3, col + 3
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row - 1][col + 1] == 1 and \
                        self._board_repo.board[row - 2][col + 2] == 0 and \
                        self._board_repo.board[row - 3][col + 3] == 1:
                    return row - 2, col + 2
                elif self._board_repo.board[row][col] == 1 and self._board_repo.board[row - 1][col + 1] == 0 and \
                        self._board_repo.board[row - 2][col + 2] == 1 and \
                        self._board_repo.board[row - 3][col + 3] == 1:
                    return row - 1, col + 1

        return None
