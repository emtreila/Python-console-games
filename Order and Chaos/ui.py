from texttable import Texttable

from order_and_chaos_var2.services import Service


class UI:
    def __init__(self, service: Service = Service):
        self._service = service

    def show_board(self):
        board = Texttable()
        for i in range(6):
            row = self._service.get_board()[i]
            board.add_row(row)
        print(board.draw())

    def main(self):
        self.show_board()

        turn = 0  # 0 for order, 1 for chaos
        first = True
        while True:
            if self._service.order_won():
                row, col, symbol = self._service.order_winning_move()
                print(f"Order's turn: ({row+1}, {col+1}, {symbol})")
                self.show_board()
                print("ORDER WINS!")
                exit()
            elif self._service.chaos_won():
                print("CHAOS WINS!")
                exit()
            else:
                if turn == 0:
                    turn = 1
                    if first:
                        row, col, symbol = self._service.order_first_move()
                        first = False
                    else:
                        if self._service.order_winning_move():
                            row, col, symbol = self._service.order_winning_move()
                            self._service.order_move(row, col, symbol)
                        else:
                            row, col, symbol = self._service.order_move_neighbours()
                    print(f"Order's turn: ({row+1}, {col+1}, {symbol})")
                    self.show_board()

                elif turn == 1:
                    turn = 0
                    while True:
                        symbol = input("Enter the symbol: ")
                        if symbol != 'X' and symbol != 'O':
                            print("Invalid symbol!")
                            continue
                        break

                    while True:
                        row = input("Enter the row: ")
                        col = input("Enter the column: ")
                        try:
                            row = int(row)
                            col = int(col)
                        except:
                            print("Invalid input!")
                            continue
                        if not (1 <= row <= 6 and 1 <= col <= 6):
                            print("Invalid input!")
                            continue
                        break
                    print(f"Chaos's turn: ({row}, {col}, {symbol})")
                    self._service.chaos_move(row-1, col-1, symbol)
                    self.show_board()
