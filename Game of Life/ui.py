from game_of_life.service import Service

import texttable as tt
import os


class UI:
    def __init__(self, service: Service = Service):
        self._service = service
        self._table = []

    def print_table(self):
        table = tt.Texttable()

        for row in self._table:
            table.add_row(row)

        print(table.draw())

    def handle_place(self, command, bl, be):
        if len(command) != 4:
            raise ValueError("The command is incorrect.")
        pattern = command[1]
        x = command[2]
        y = command[3]

        try:
            x = int(x)
            y = int(y)
        except:
            raise ValueError("The coordinates must be integers.")

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise ValueError("The coordinates are not in the board!")

        if pattern not in ["block", "blinker", "tub", "beacon", "spaceship"]:
            raise ValueError("The pattern is not in the list!")

        file_name = ""

        if pattern == "block":
            file_name = os.path.join("patterns", "block.txt")
        elif pattern == "blinker":
            if bl == 0:
                bl = 1
                file_name = os.path.join("patterns", "blinker1.txt")

            else:
                bl = 0
                file_name = os.path.join("patterns", "blinker2.txt")

        elif pattern == "tub":
            file_name = os.path.join("patterns", "tub.txt")
        elif pattern == "beacon":
            if be == 0:
                be = 1
                file_name = os.path.join("patterns", "beacon1.txt")

            else:
                be = 0
                file_name = os.path.join("patterns", "beacon2.txt")

        elif pattern == "spaceship":
            file_name = os.path.join("patterns", "spaceship.txt")

        pattern = self._service.get_pattern(file_name)
        self._service.place_pattern(pattern, x, y, self._table)
        self.print_table()

    def handle_tick(self, command):
        if len(command) == 1:
            self._table = self._service.tick(self._table)
            self.print_table()

        elif len(command) == 2:
            n = command[1]
            try:
                n = int(n)
            except:
                raise ValueError("The number of ticks must be an integer.")

            current = self._table
            for i in range(n):
                self._table = self._service.tick(current)
                current = self._table

            self.print_table()

        else:
            raise ValueError("The command is incorrect.")

    def handle_save(self, command):
        if len(command) != 2:
            raise ValueError("The command is incorrect.")
        self._service.save_to_file(self._table)

    def handle_load(self, command):
        if len(command) != 2:
            raise ValueError("The command is incorrect.")
        self._table = self._service.load_from_file()
        self.print_table()

    def main(self):
        for i in range(8):
            row = ["_" for j in range(8)]
            self._table.append(row)

        self.print_table()

        commands = {
            "place": self.handle_place,
            "tick": self.handle_tick,
            "save": self.handle_save,
            "load": self.handle_load
        }

        print("\nCOMMANDS:")
        print("place <pattern> <x,y>")
        print("tick [n]")
        print("save simulation.txt")
        print("load simulation.txt")

        bl = 0
        be = 0

        while True:
            command = input("\nEnter command: ")
            if not command:
                print("No command given!")
                continue
            arguments = command.split()
            command_name = arguments[0].strip()

            handle_for_command = commands.get(command_name)
            if not handle_for_command:
                print(f"Command {command_name} is not accepted!")
                continue

            try:
                if command_name == "place":
                    handle_for_command(arguments, bl, be)

                if command_name == "tick":
                    handle_for_command(arguments)

                if command_name == "save":
                    handle_for_command(arguments)

                if command_name == "load":
                    handle_for_command(arguments)

            except Exception as e:
                print(e)
