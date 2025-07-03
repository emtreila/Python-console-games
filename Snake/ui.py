from texttable import Texttable

from snake.services import Service


class UI:
    def __init__(self, service: Service = Service):
        self._service = service
        self._direction = "up"
        self._last_direction = "up"
        self.snake_head_i, self.snake_head_j = self._service.get_snake_head()
        self.n = int(self._service.get_settings().get("n"))

    def show_board(self):
        board = Texttable()
        for i in range(int(self._service.get_settings().get("n"))):
            row = self._service.get_board()[i]
            board.add_row(row)

        print(board.draw())

    def handle_move(self, arguments):
        if len(arguments) == 1:
            if not self._service.move_snake(self._direction):
                print("GAME OVER! YOU HIT YOURSELF!")
                exit()

        elif len(arguments) == 2:
            positions = arguments[1].strip()

            try:
                positions = int(positions)
            except:
                print("Invalid number of positions!")
                return
            if not (self._service.check_positions(positions, self._direction)):
                print("GAME OVER! YOU HIT THE EDGE!")
                exit()
            else:
                for _ in range(positions):
                    if not self._service.move_snake(self._direction):
                        print("GAME OVER! YOU HIT YOURSELF!")
                        exit()

        self.show_board()

    def handle_direction(self, arguments):
        if (self._direction == "up" and arguments[0].strip() == "down") or (
                self._direction == "down" and arguments[0].strip() == "up") or (
                self._direction == "right" and arguments[0].strip() == "left") or (
                self._direction == "left" and arguments[0].strip() == "right"):
            print("Invalid move!")
            return

        elif len(arguments) == 1:
            if arguments[0].strip() == "up":
                self._last_direction = self._direction
                self._direction = "up"
            elif arguments[0].strip() == "right":
                self._last_direction = self._direction
                self._direction = "right"
            elif arguments[0].strip() == "down":
                self._last_direction = self._direction
                self._direction = "down"
            elif arguments[0].strip() == "left":
                self._last_direction = self._direction
                self._direction = "left"

    def main(self):
        self.show_board()

        print("move [n]")
        print("up | right | down | left")

        while True:
            commands = {
                "move": self.handle_move,
                "up": self.handle_direction,
                "right": self.handle_direction,
                "down": self.handle_direction,
                "left": self.handle_direction
            }

            command = input("Enter your command: ")
            if not command:
                print("No command given!")

            arguments = command.split()
            command_name = arguments[0].strip()

            handle_for_command = commands.get(command_name)
            if not handle_for_command:
                print(f"Command {command_name} not accepted!")

            try:
                if command_name == "move":
                    handle_for_command(arguments)
                elif command_name == "up" or command_name == "right" or command_name == "down" or command_name == "left":
                    handle_for_command(arguments)
            except Exception as e:
                print(e)
