from hammurabi.game import Game


class Repo:
    def __init__(self):
        self._games = []
        self._current_game = None

    @property
    def games(self):
        return self._games

    @property
    def current_game(self):
        return self._current_game

    @current_game.setter
    def current_game(self, value):
        self._current_game = value

    def add_game(self, game):
        self._games.append(game)

    def start_game(self):
        self._current_game = Game()
        self.add_game(self._current_game)
