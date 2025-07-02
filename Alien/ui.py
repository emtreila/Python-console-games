from texttable import Texttable

from alien.services import Service


class UI:
    def __init__(self, service: Service = Service):
        self._service = service
        self._first_round = True

    def show_board(self):
        board = Texttable()

        header = [" "] + [str(i) for i in range(1, 8)]
        board.header(header)

        for i, row_label in enumerate("ABCDEFG"):
            row = [row_label] + self._service.get_board()[i]
            board.add_row(row)

        print(board.draw())

    def show_board_to_player(self, board_without_aliens):
        board = Texttable()

        header = [" "] + [str(i) for i in range(1, 8)]
        board.header(header)

        for i, row_label in enumerate("ABCDEFG"):
            row = [row_label] + board_without_aliens[i]
            board.add_row(row)

        print(board.draw())

    def handle_fire(self, arguments):
        if len(arguments) != 2:
            print("Invalid command!")
            return
        coord = arguments[1]
        if len(coord) != 2:
            print("Invalid coordinate!")
            return

        letter = coord[0]
        number = coord[1]
        if not letter in "ABCDEFGH":
            print("Invalid coordinate!")
            return
        if not number in "12345678":
            print("Invalid coordinate!")
            return

        fire_row, fire_col = self._service.transform_coordinates(coord)
        board_symbol = self._service.get_board()[fire_row][fire_col]
        can_continue = True

        if board_symbol == "":
            can_continue = self._service.move_aliens(fire_row, fire_col)
        elif board_symbol in "*-":
            can_continue = self._service.move_aliens(fire_row, fire_col)
            print("There is an asteroid! Try again!")
        elif board_symbol == "X":
            can_continue = self._service.move_aliens(fire_row, fire_col)
            print(f"Alien ship destroyed! Remaining: {self._service.get_aliens_remaining()}")

        # Checking game conditions
        is_win = self._service.check_win()
        game_over = not can_continue or is_win

        if is_win:
            print("GAME WON! ALIEN SHIPS DESTROYED!")

        if not can_continue:
            print("GAME OVER! ALIEN SHIPS WON!")

        self.show_board_to_player(self._service.get_board())
        if game_over:
            exit()

    def handle_cheat(self, arguments):
        if len(arguments) != 1:
            print("Invalid command!")
            return
        else:
            self.show_board()

    def main(self):
        board_without_aliens = self._service.get_board_without_aliens()
        self.show_board_to_player(board_without_aliens)

        commands = {
            "fire": self.handle_fire,
            "cheat": self.handle_cheat
        }

        print("\nCOMMANDS:")
        print("fire <coordinate>")
        print("cheat\n")

        while True:
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
                handle_for_command(arguments)
            except Exception as e:
                print(e)
