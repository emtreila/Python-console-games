import random


class Repo:
    def __init__(self):
        self._board = []
        self._snake = []
        self._snake_tail = None
        self._settings = {}
        self.__read_settings()
        self.__create_board()
        self._n = int(self._settings.get("n"))

    @property
    def board(self):
        return self._board

    @property
    def settings(self):
        return self._settings

    def __read_settings(self):
        with open("settings.properties", "r") as f:
            for line in f.readlines():
                key, value = line.strip().split("=")
                self._settings[key] = value

    def __create_board(self):
        """
        Create the board the game is played on
        """

        self._board = [["" for _ in range(int(self._settings.get("n")))] for _ in range(int(self._settings.get("n")))]
        middle = int(self._settings.get("n")) // 2

        self._board[middle - 1][middle] = "*"
        self._snake.append([middle - 1, middle])

        self._board[middle][middle] = "+"
        self._snake.append([middle, middle])

        self._board[middle + 1][middle] = "+"
        self._snake.append([middle + 1, middle])
        self._snake_tail = [middle + 1, middle]

        apples = int(self._settings.get("apples"))
        for i in range(apples):
            while True:
                random_row = random.randint(0, int(self._settings.get("n")) - 1)
                random_col = random.randint(0, int(self._settings.get("n")) - 1)
                if self._board[random_row][random_col] == "":
                    self._board[random_row][random_col] = "a"
                    break

    def is_apple(self, apple_position):
        """
        Check if the snake has eaten an apple
        """
        x, y = apple_position

        if self._board[x][y] == "a":
            self._snake.append(self._snake_tail)

            self._board[self._snake_tail[0]][self._snake_tail[1]] = "+"  # add a body segment

            while True:
                random_row = random.randint(0, int(self._settings.get("n")) - 1)
                random_col = random.randint(0, int(self._settings.get("n")) - 1)
                if self._board[random_row][random_col] == "":
                    self._board[random_row][random_col] = "a"
                    break

    def check_segment(self, direction):
        """
        Check if the snake has hit itself
        """
        if direction == "up":
            if self._board[self._snake[0][0] - 1][self._snake[0][1]] == "+":
                return True
        elif direction == "right":
            if self._board[self._snake[0][0]][self._snake[0][1] + 1] == "+":
                return True
        elif direction == "down":
            if self._board[self._snake[0][0] + 1][self._snake[0][1]] == "+":
                return True
        elif direction == "left":
            if self._board[self._snake[0][0]][self._snake[0][1] - 1] == "+":
                return True
        return False

    def move_up(self):
        """
        Move the snake up
        """

        self._board[self._snake_tail[0]][self._snake_tail[1]] = ""

        new_head = [self._snake[0][0] - 1, self._snake[0][1]]  # new head position

        apple_position = new_head  # check for apple
        self.is_apple(apple_position)

        new_snake = [new_head] + self._snake[:-1]
        self._snake = new_snake

        self._board[new_head[0]][new_head[1]] = "*"
        for x, y in self._snake[1:]:
            self._board[x][y] = "+"

        self._snake_tail = self._snake[-1]

    def move_down(self):
        """
        Move the snake down
        """

        self._board[self._snake[-1][0]][self._snake[-1][1]] = ""

        new_head = [self._snake[0][0] + 1, self._snake[0][1]]

        self.is_apple(new_head)

        new_snake = [new_head] + self._snake[:-1]
        self._snake = new_snake

        self._board[new_head[0]][new_head[1]] = "*"
        for x, y in self._snake[1:]:
            self._board[x][y] = "+"

        self._snake_tail = self._snake[-1]

    def move_right(self):
        """
        Move the snake to the right
        """
        self._board[self._snake[-1][0]][self._snake[-1][1]] = ""

        new_head = [self._snake[0][0], self._snake[0][1] + 1]

        self.is_apple(new_head)

        new_snake = [new_head] + self._snake[:-1]
        self._snake = new_snake

        self._board[new_head[0]][new_head[1]] = "*"
        for x, y in self._snake[1:]:
            self._board[x][y] = "+"

        self._snake_tail = self._snake[-1]

    def move_left(self):
        """
        Move the snake to the left
        """
        self._board[self._snake[-1][0]][self._snake[-1][1]] = ""

        new_head = [self._snake[0][0], self._snake[0][1] - 1]

        self.is_apple(new_head)

        new_snake = [new_head] + self._snake[:-1]
        self._snake = new_snake

        self._board[new_head[0]][new_head[1]] = "*"
        for x, y in self._snake[1:]:
            self._board[x][y] = "+"

        self._snake_tail = self._snake[-1]
