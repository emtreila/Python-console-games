class Board:
    def __init__(self, row, col):
        self._row = row
        self._col = col

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, new):
        self._row = new

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, new):
        self._col = new
    