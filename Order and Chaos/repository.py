import random


class Repo:
    def __init__(self):
        self._board = [[' ' for _ in range(6)] for _ in range(6)]

    def get_board(self):
        """
        :return: the board
        """
        return self._board

    def get_symbol(self):
        """
        Decides which symbol does order play with
        :return: the symbol
        """
        X = 0
        O = 0
        for _ in range(6):
            for j in range(6):
                if self._board[_][j] == 'X':
                    X += 1
                elif self._board[_][j] == 'O':
                    O += 1
        if X >= O:
            symbol = "X"
        else:
            symbol = "O"
        return symbol

    def order_neighbours_move(self):
        """
        Order places a symbol on the square that has the most neighbours of the same symbol
        """
        symbol = self.get_symbol()
        max_neighbours = 0
        row = 0
        col = 0
        for i in range(6):
            for j in range(6):
                if self._board[i][j] == ' ':
                    neighbours = 0
                    if i - 1 >= 0 and self._board[i - 1][j] == symbol:
                        neighbours += 1
                    if i + 1 < 6 and self._board[i + 1][j] == symbol:
                        neighbours += 1
                    if j - 1 >= 0 and self._board[i][j - 1] == symbol:
                        neighbours += 1
                    if j + 1 < 6 and self._board[i][j + 1] == symbol:
                        neighbours += 1
                    if i - 1 >= 0 and j - 1 >= 0 and self._board[i - 1][j - 1] == symbol:
                        neighbours += 1
                    if i - 1 >= 0 and j + 1 < 6 and self._board[i - 1][j + 1] == symbol:
                        neighbours += 1
                    if i + 1 < 6 and j - 1 >= 0 and self._board[i + 1][j - 1] == symbol:
                        neighbours += 1
                    if i + 1 < 6 and j + 1 < 6 and self._board[i + 1][j + 1] == symbol:
                        neighbours += 1
                    if neighbours > max_neighbours:
                        max_neighbours = neighbours
                        row = i
                        col = j
        self._board[row][col] = symbol
        return row, col, symbol

    def order_winning_move(self):
        """
        If there are 4 pieces put by chaos such that it can win the game with the next move, it puts the 5th piece
        :return: the row, column and symbol for which the next move wins the game
        """
        symbol = self.get_symbol()
        board = self._board
        # Check to see if we have 5 pieces in a row HORIZONTALLY
        for row in range(6):
            for col in range(2):
                if board[row][col] == symbol and board[row][col + 1] == symbol \
                        and board[row][col + 2] == symbol and \
                        board[row][col + 3] == symbol and board[row][col + 4] == ' ':
                    return row, col + 4, symbol
                elif board[row][col] == symbol and board[row][col + 1] == symbol \
                        and board[row][col + 2] == symbol and \
                        board[row][col + 3] == ' ' and board[row][col + 4] == symbol:
                    return row, col + 3, symbol
                elif board[row][col] == symbol and board[row][col + 1] == symbol \
                        and board[row][col + 2] == ' ' and \
                        board[row][col + 3] == symbol and board[row][col + 4] == symbol:
                    return row, col + 2, symbol
                elif board[row][col] == symbol and board[row][col + 1] == ' ' \
                        and board[row][col + 2] == symbol and \
                        board[row][col + 3] == symbol and board[row][col + 4] == symbol:
                    return row, col + 1, symbol
                elif board[row][col] == ' ' and board[row][col + 1] == symbol \
                        and board[row][col + 2] == symbol and \
                        board[row][col + 3] == symbol and board[row][col + 4] == symbol:
                    return row, col, symbol

        # Check to see if we have 5 pieces in a row VERTICALLY
        for col in range(6):
            for row in range(2):
                if board[row][col] == symbol and board[row + 1][col] == symbol \
                        and board[row + 2][col] == symbol and \
                        board[row + 3][col] == symbol and board[row + 4][col] == ' ':
                    return row + 4, col, symbol
                elif board[row][col] == symbol and board[row + 1][col] == symbol \
                        and board[row + 2][col] == symbol and \
                        board[row + 3][col] == ' ' and board[row + 4][col] == symbol:
                    return row + 3, col, symbol
                elif board[row][col] == symbol and board[row + 1][col] == symbol \
                        and board[row + 2][col] == ' ' and \
                        board[row + 3][col] == symbol and board[row + 4][col] == symbol:
                    return row + 2, col, symbol
                elif board[row][col] == symbol and board[row + 1][col] == ' ' \
                        and board[row + 2][col] == symbol and \
                        board[row + 3][col] == symbol and board[row + 4][col] == symbol:
                    return row + 1, col, symbol
                elif board[row][col] == ' ' and board[row + 1][col] == symbol \
                        and board[row + 2][col] == symbol and \
                        board[row + 3][col] == symbol and board[row + 4][col] == symbol:
                    return row, col, symbol

        # Check to see if we have 5 pieces in a row DIAGONALLY
        for i in range(2):
            if board[0 + i][0 + i] == symbol and board[1 + i][1 + i] == symbol and board[2 + i][2 + i] == symbol \
                    and board[3 + i][3 + i] == symbol and board[4 + i][4 + i] == ' ':
                return 4 + i, 4 + i, symbol
            elif board[0 + i][0 + i] == symbol and board[1 + i][1 + i] == symbol and board[2 + i][2 + i] == symbol \
                    and board[3 + i][3 + i] == ' ' and board[4 + i][4 + i] == symbol:
                return 3 + i, 3 + i, symbol
            elif board[0 + i][0 + i] == symbol and board[1 + i][1 + i] == symbol and board[2 + i][2 + i] == ' ' \
                    and board[3 + i][3 + i] == symbol and board[4 + i][4 + i] == symbol:
                return 2 + i, 2 + i, symbol
            elif board[0 + i][0 + i] == symbol and board[1 + i][1 + i] == ' ' and board[2 + i][2 + i] == symbol \
                    and board[3 + i][3 + i] == symbol and board[4 + i][4 + i] == symbol:
                return 1 + i, 1 + i, symbol
            elif board[0 + i][0 + i] == ' ' and board[1 + i][1 + i] == symbol and board[2 + i][2 + i] == symbol \
                    and board[3 + i][3 + i] == symbol and board[4 + i][4 + i] == symbol:
                return 0 + i, 0 + i, symbol
            if board[0 + i][5 - i] == symbol and board[1 + i][4 - i] == symbol and board[2 + i][3 - i] == symbol \
                    and board[3 + i][2 - i] == symbol and board[4 + i][1 - i] == ' ':
                return 4 + i, 1 - i, symbol
            elif board[0 + i][5 - i] == symbol and board[1 + i][4 - i] == symbol and board[2 + i][3 - i] == symbol \
                    and board[3 + i][2 - i] == ' ' and board[4 + i][1 - i] == symbol:
                return 3 + i, 2 - i, symbol
            elif board[0 + i][5 - i] == symbol and board[1 + i][4 - i] == symbol and board[2 + i][3 - i] == ' ' \
                    and board[3 + i][2 - i] == symbol and board[4 + i][1 - i] == symbol:
                return 2 + i, 3 - i, symbol
            elif board[0 + i][5 - i] == symbol and board[1 + i][4 - i] == ' ' and board[2 + i][3 - i] == symbol \
                    and board[3 + i][2 - i] == symbol and board[4 + i][1 - i] == symbol:
                return 1 + i, 4 - i, symbol
            elif board[0 + i][5 - i] == ' ' and board[1 + i][4 - i] == symbol and board[2 + i][3 - i] == symbol \
                    and board[3 + i][2 - i] == symbol and board[4 + i][1 - i] == symbol:
                return 0 + i, 5 - i, symbol

        return None

    def chaos_move(self, row, col, symbol):
        """
        Chaos makes a move
        """
        self._board[row][col] = symbol

    def order_first_move(self):
        """
        Order makes the first move
        :return: the row, column and symbol for the first move
        """
        symbol = self.get_symbol()
        while True:
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            if self._board[row][col] == ' ':
                self._board[row][col] = symbol
                break
        return row, col, symbol

    def order_move(self, row, col, symbol):
        """
        Order makes a move
        """
        self._board[row][col] = symbol
