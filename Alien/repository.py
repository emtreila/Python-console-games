import random


class Repo:
    def __init__(self):
        self._board = [["" for _ in range(7)] for _ in range(7)]
        self._closer = 3
        self._alien1: tuple | None = None
        self._alien1_destroyed = False
        self._alien2: tuple | None = None
        self._alien2_destroyed = False
        self._aliens_remaining = 2

        self.earth_coordinates = (3, 3)
        self._fired_coordinates = set(self.earth_coordinates)
        self._board[3][3] = "E"

        self.place_random_asteroids()
        self.place_alien_ship()

    @property
    def board(self):
        return self._board

    @property
    def aliens_remaining(self):
        return self._aliens_remaining

    def is_in_board(self, row, col):
        """
        check if x[row][col] is on board
        :param row: the row in the board
        :param col: the col in the board
        :return: True = its in the board, False = otherwise
        """
        return 0 <= row < 7 and 0 <= col < 7

    def place_random_asteroids(self):
        """
        Places 8 random adjacent asteroids
        :return: the new board
        """
        dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for _ in range(8):
            generated = False
            while not generated:
                row = random.randint(0, 6)
                col = random.randint(0, 6)
                valid = True

                for (di, dj) in dirs:
                    new_row = row + di
                    new_col = col + dj
                    if not self.is_in_board(new_row, new_col):
                        continue

                    if self._board[row][col] == "E":
                        valid = False
                        break

                    if self._board[new_row][new_col] != "":
                        valid = False
                        break

                if valid:
                    self._board[row][col] = "*"
                    generated = True

    def place_alien_ship(self):
        """
        Places the alien ship on the board
        """
        if not self._alien1_destroyed and self._alien1:
            self._board[self._alien1[0]][self._alien1[1]] = ""
        if not self._alien2_destroyed and self._alien2:
            self._board[self._alien2[0]][self._alien2[1]] = ""

        generated = False
        while not generated and not self._alien1_destroyed:
            row = random.choice([3 - self._closer, self._closer + 3])
            col = random.randint(0, 6)
            if self._board[row][col] == "" and (row, col) not in self._fired_coordinates \
                    and (row, col) != self._alien2:
                self._board[row][col] = "X"
                generated = True
                self._alien1 = (row, col)

        generated = False
        while not generated and not self._alien2_destroyed:
            row = random.randint(0, 6)
            col = random.choice([3 - self._closer, self._closer + 3])
            if self._board[row][col] == "" and (row, col) not in self._fired_coordinates \
                    and (row, col) != self._alien1:
                self._board[row][col] = "X"
                generated = True
                self._alien2 = (row, col)

    def mark_alien_as_destroyed(self, alien):
        if alien == 1:
            self._alien1 = None
            self._alien1_destroyed = True
        else:
            self._alien2 = None
            self._alien2_destroyed = True

        self._aliens_remaining -= 1

    def move_aliens(self, fire_x, fire_y):
        """
        Moves the aliens

        Marks the aliens as destroyed if they are hit
        :param fire_x: The x coordinate of the fire
        :param fire_y: The y coordinate of the fire
        :return: True if the aliens did not win yet, False otherwise
        """
        if (fire_x, fire_y) not in self._fired_coordinates:
            if self.board[fire_x][fire_y] == "X":
                if self._alien1 == (fire_x, fire_y):
                    self.mark_alien_as_destroyed(1)
                elif self._alien2 == (fire_x, fire_y):
                    self.mark_alien_as_destroyed(2)
                self._fired_coordinates.add((fire_x, fire_y))

            if self._board[fire_x][fire_y] not in ["*", "-"]:
                self._fired_coordinates.add((fire_x, fire_y))
                self._board[fire_x][fire_y] = "-"

        closer_to_Earth = random.randint(0, 1)
        if closer_to_Earth > 0.5:
            self._closer -= 1
        print(self._closer)
        self.place_alien_ship()

        # Verifying if the aliens are adjacent to Earth
        if self._alien1:
            print(self._alien1)
            if abs(self._alien1[0] - self.earth_coordinates[0]) == 1 and abs(
                    self._alien1[1] - self.earth_coordinates[1]) == 1:
                return False
        if self._alien2:
            print(self._alien2)
            if abs(self._alien2[0] - self.earth_coordinates[0]) == 1 and abs(
                    self._alien2[1] - self.earth_coordinates[1]) == 1:
                return False

        return True
