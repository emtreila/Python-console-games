from snake.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self._repo = repo

    def get_snake_head(self):
        """
        :return: the head of the snake
        """
        for i in range(len(self._repo.board)):
            for j in range(len(self._repo.board[i])):
                if self._repo.board[i][j] == "*":
                    return i, j

    def get_board(self):
        """
        :return: the board the game is played on
        """
        return self._repo.board

    def get_settings(self):
        """
        :return: the settings
        """
        return self._repo.settings

    def move_snake(self, direction):
        """
        Move the snake in the given direction
        :param direction: the direction the snake should move in
        """
        if not self.check_segments(direction):
            if direction == "up":
                self._repo.move_up()
                return True
            elif direction == "right":
                self._repo.move_right()
                return True
            elif direction == "down":
                self._repo.move_down()
                return True
            elif direction == "left":
                self._repo.move_left()
                return True
        else:
            return False

    def check_positions(self, positions, direction):
        """
        Check if the number of positions is valid
        :param positions: the number of positions
        :param direction: the direction the snake should move in
        :return: True if the number of positions is valid, False otherwise
        """
        snake_head_i, snake_head_j = self.get_snake_head()
        n = int(self.get_settings().get("n"))
        if direction == "up":
            if positions > snake_head_i:
                return False
        elif direction == "right":
            if positions > n - snake_head_j:
                return False
        elif direction == "down":
            if positions > n - snake_head_i:
                return False
        elif direction == "left":
            if positions > snake_head_j:
                return False
        return True

    def check_segments(self, direction):
        """
        Check if the snake has hit itself
        :return: True if the snake has hit itself, False otherwise
        """
        return self._repo.check_segment(direction)
