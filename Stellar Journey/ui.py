from stellar_journey.services import Service
from texttable import Texttable


class UI:
    def __init__(self, service: Service = Service):
        self._service = service
        self._cruisers = 3

    def show_board(self):
        board = Texttable()

        header = [" "] + [str(i) for i in range(1, 9)]
        board.header(header)

        for i, row_label in enumerate("ABCDEFGH"):
            row = [row_label] + self._service.get_board()[i]
            board.add_row(row)

        print(board.draw())

    def show_adjacent_board(self, adj_board):
        board = Texttable()

        header = [" "] + [str(i) for i in range(1, 9)]
        board.header(header)

        for i, row_label in enumerate("ABCDEFGH"):
            row = [row_label] + adj_board[i]
            board.add_row(row)

        print(board.draw())

    def handle_warp(self, arguments, row_E, col_E):
        if len(arguments) != 2:
            print("Invalid command!")
            return
        k = 0
        coord = arguments[1]
        letter = coord[0]
        number = coord[1]
        for l in "ABCDEFGH":
            if l == letter:
                k = 1
        if k == 0:
            print("Invalid coordinate!")
            return
        k = 0
        for n in "12345678":
            if n == number:
                k = 1
        if k == 0:
            print("Invalid coordinate!")
            return
        new_row, new_col = self._service.transform_coordinates(coord)

        if new_row == row_E or new_col == col_E or abs(new_row - row_E) == abs(new_col - col_E):
            if self._service.get_board()[new_row][new_col] == "":
                self._service.change_E_coord(new_row, new_col)
            elif self._service.get_board()[new_row][new_col] == "*":
                print("You cannot warp over a star!")
            elif self._service.get_board()[new_row][new_col] == "B":
                print("GAME OVER! YOU WARPED INTO A BLINGON CRUISER!")
                exit()
        else:
            print("Can't wrap there!")

        self.show_adjacent_board(self._service.board_with_adjacent_cruisers())

    def handle_fire(self, arguments):
        if len(arguments) != 2:
            print("Invalid command!")
            return
        k = 0
        coord = arguments[1]
        letter = coord[0]
        number = coord[1]
        for l in "ABCDEFGH":
            if l == letter:
                k = 1
        if k == 0:
            print("Invalid coordinate!")
            return
        k = 0
        for n in "12345678":
            if n == number:
                k = 1
        if k == 0:
            print("Invalid coordinate!")
            return

        fire_row, fire_col = self._service.transform_coordinates(coord)
        adj_coords = self._service.adjacent_coordinates()
        if (fire_row, fire_col) in adj_coords:
            if self._service.get_board()[fire_row][fire_col] == "B":
                print("You hit a Blingon cruiser!")
                self._service.get_board()[fire_row][fire_col] = ""
                self._cruisers -= 1
                self._service.place_random_cruisers(self._cruisers)
                self.show_adjacent_board(self._service.board_with_adjacent_cruisers())

            else:
                print("You missed!")
        else:
            print("Invalid coordinate!")



    def handle_cheat(self, arguments):
        if len(arguments) != 1:
            print("Invalid command!")
            return
        else:
            self.show_board()

    def main(self):
        adj_board = self._service.board_with_adjacent_cruisers()
        self.show_adjacent_board(adj_board)

        commands = {
            "warp": self.handle_warp,
            "fire": self.handle_fire,
            "cheat": self.handle_cheat
        }

        print("\nCOMMANDS:")
        print("warp <coordinate>")
        print("fire <coordinate>")
        print("cheat\n")

        while True:
            if self._service.check_win():
                print("GAME WON! ALL BLINGON CRUISERS DESTROYED!")
                exit()

            command = input("Enter your command: ")
            if not command:
                print("No command given!")
                continue

            arguments = command.split()
            command_name = arguments[0].strip()

            handle_for_command = commands.get(command_name)
            if not handle_for_command:
                print(f"Command {command_name} not accepted!")
                continue

            try:
                if command_name == "warp":
                    handle_for_command(arguments, self._service.get_row_E(), self._service.get_col_E())
                elif command_name == "fire":
                    handle_for_command(arguments)
                elif command_name == "cheat":
                    handle_for_command(arguments)

            except Exception as e:
                print(e)
