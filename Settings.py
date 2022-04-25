class Settings:
    def __init__(self):
        self._row_count = 12
        self._col_count = 12
        self._color_count = 6

    @property
    def row_count(self) -> int:
        return self._row_count

    @row_count.setter
    def row_count(self, a):
        self._row_count = a

    @property
    def col_count(self) -> int:
        return self._col_count

    @col_count.setter
    def col_count(self, a):
        self._col_count = a

    @property
    def color_count(self) -> int:
        return self._color_count

    @color_count.setter
    def color_count(self, a):
        self._color_count = a
