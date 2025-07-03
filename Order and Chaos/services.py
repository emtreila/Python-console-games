from order_and_chaos_var2.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self._repo = repo

    def get_board(self):
        """
        :return: the board
        """
        return self._repo.get_board()

    def order_move_neighbours(self):
        """
        Order makes a move
        """
        return self._repo.order_neighbours_move()

    def order_winning_move(self):
        """
        Order makes a move
        """
        return self._repo.order_winning_move()

    def order_move(self, row, col, symbol):
        """
        Order makes a move
        """
        self._repo.order_move(row, col, symbol)

    def chaos_move(self, row, col, symbol):
        """
        Chaos makes a move
        """
        self._repo.chaos_move(row, col, symbol)

    def order_first_move(self):
        """
        Order makes the first move
        """
        return self._repo.order_first_move()

    def order_won(self):
        """
        Check if order wins
        """
        symbol = self._repo.get_symbol()
        board = self._repo.get_board()
        # Check to see if we have 5 pieces in a row HORIZONTALLY
        for row in range(6):  # 2 because we cant have 5 in a row on position 2,3,4,5
            for col in range(2):
                if board[row][col] == symbol and board[row][col + 1] == symbol \
                        and board[row][col + 2] == symbol and \
                        board[row][col + 3] == symbol and board[row][col + 4] == symbol:
                    return True

        # Check to see if we have 5 pieces in a row VERTICALLY
        for col in range(6):
            for row in range(2):
                if board[row][col] == symbol and board[row + 1][col] == symbol \
                        and board[row + 2][col] == symbol and \
                        board[row + 3][col] == symbol and board[row + 4][col] == symbol:
                    return True

        # Check to see if we have 5 pieces in a row DIAGONALLY ( / and \ )
        for i in range(2):
            if board[0 + i][0 + i] == symbol and board[1 + i][1 + i] == symbol and board[2 + i][
                2 + i] == symbol \
                    and board[3 + i][3 + i] == symbol and board[4 + i][4 + i] == symbol:
                return True

            if board[0 + i][5 - i] == symbol and board[1 + i][4 - i] == symbol and board[2 + i][3 - i] == symbol \
                    and board[3 + i][2 - i] == symbol and board[4 + i][1 - i] == symbol:
                return True

        # Above/Below FIRST and SECOND DIAGONALS

        # Above/Below FIRST DIAGONAL
        if board[0][1] == symbol and board[1][2] == symbol and board[2][3] == symbol and board[3][4] == symbol and \
                board[4][5] == symbol:
            return True

        if board[1][0] == symbol and board[2][1] == symbol and board[3][2] == symbol and board[4][3] == symbol and \
                board[5][4] == symbol:
            return True

        # Above/Below SECOND DIAGONAL
        if board[0][4] == symbol and board[1][3] == symbol and board[2][2] == symbol and board[3][1] == symbol and \
                board[4][0] == symbol:
            return True

        if board[1][5] == symbol and board[2][4] == symbol and board[3][3] == symbol and board[4][2] == symbol and \
                board[5][1] == symbol:
            return True

        return False

    def chaos_won(self):
        """
        Check if chaos wins
        """
        for i in range(6):
            for j in range(6):
                if self._repo.get_board()[i][j] == ' ':
                    return False
        return True
