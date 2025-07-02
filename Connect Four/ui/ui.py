import random

from service.service import Service


class UI:

    def __init__(self, service: Service):
        self._service = service

    def main(self):
        game_over = False
        user = 0
        computer = 1
        turn = random.randint(0, 1)  # choose at random who starts the game
        while not game_over:
            print(self._service.print_board())

            if self._service.is_tie():
                print("It's a tie!")
                break

            if turn == user:
                move = input("Make your move (0-6): ")

                try:
                    move = int(move)
                except:
                    print("Invalid move!")
                    continue

                if not (0 <= move <= 6):
                    print("Invalid move!")
                    continue
                if not (self._service.is_valid_location(move)):
                    print("The column has already 6 pieces!")
                    continue
                else:
                    row = self._service.get_open_row(move)
                    self._service.put_piece(row, move, 1)
                    turn += 1
                    turn = turn % 2

                if self._service.is_won(1):
                    print(self._service.print_board())
                    print("YOU WON!")
                    game_over = True

            if turn == computer and not game_over:
                if not self._service.winning_move_computer():  # if the computer cant win with the next move
                    # it tries to block the users winning move if there is one
                    if not self._service.winning_move_user():
                        move = random.randint(0, 6)
                        print(f"Computers move: {move}")
                        row = self._service.get_open_row(move)
                        self._service.put_piece(row, move, 2)

                    else:
                        row, col = self._service.winning_move_user()
                        if self._service.is_valid_row(col, row):
                            print(f"Computers move: {col}")
                            self._service.put_piece(row, col, 2)
                        else:
                            move = random.randint(0, 6)
                            print(f"Computers move: {move}")
                            row = self._service.get_open_row(move)
                            self._service.put_piece(row, move, 2)

                else:
                    row, col = self._service.winning_move_computer()
                    print(f"Computers move: {col}")
                    self._service.put_piece(row, col, 2)

                turn += 1
                turn = turn % 2

                if self._service.is_won(2):
                    print(self._service.print_board())
                    print("YOU LOST!")
                    game_over = True
