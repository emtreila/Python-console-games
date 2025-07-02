import numpy as np


class MemoRepo:
    def __init__(self):
        self._board = np.zeros((6, 7))

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new_board):
        self._board = new_board

    def put_piece(self, row, col, piece):
        """
        Puts the piece on the board
        :param row: the row the piece is put on
        :param col: the column the piece is put on
        :param piece: the piece 1 = user   2 = computer
        """
        self._board[row][col] = piece