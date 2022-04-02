import random as rnd
from color_constant import colors
from enum import Enum


class RepaintGameState(Enum):
    NOT_PLAYING = 0
    PLAYING = 1
    WIN = 2


class Cell:
    def __init__(self, color_count):
        self._color = rnd.choice(list(colors.keys())[:color_count])
        self._is_painted = False
        self._neighbours = [None, None, None, None]

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, a):
        self._color = a

    @property
    def is_painted(self) -> bool:
        return self._is_painted

    @is_painted.setter
    def is_painted(self, a):
        self._is_painted = a

    @property
    def left(self):
        return self._neighbours[0]

    @left.setter
    def left(self, a):
        self._neighbours[0] = a

    @property
    def up(self):
        return self._neighbours[1]

    @up.setter
    def up(self, a):
        self._neighbours[1] = a

    @property
    def right(self):
        return self._neighbours[2]

    @right.setter
    def right(self, a):
        self._neighbours[2] = a

    @property
    def down(self):
        return self._neighbours[3]

    @down.setter
    def down(self, a):
        self._neighbours[3] = a


class RepaintGame:
    def __init__(self, row_count: int, col_count: int, color_count: int):
        self._first_cell = None
        self._row_count = row_count
        self._col_count = col_count
        self._color_count = color_count
        self._state = RepaintGameState.NOT_PLAYING
        self.new_game()

    def new_game(self) -> None:
        self._first_cell = Cell(self.color_count)
        self._first_cell.is_painted = True
        curr_cell = None
        left_cell = None
        up_cell = None
        for i in range(self.row_count):
            for j in range(self.col_count):
                if j == 0:
                    if i == 0:
                        curr_cell = self._first_cell
                    else:
                        curr_cell = Cell(self.color_count)
                    up_cell = self._first_cell
                    for _ in range(i - 1):
                        up_cell = up_cell.down
                else:
                    if i > 0:
                        up_cell = up_cell.right
                    left_cell = curr_cell
                    curr_cell = Cell(self.color_count)
                if i != 0:
                    curr_cell.up = up_cell
                    up_cell.down = curr_cell
                if j != 0:
                    curr_cell.left = left_cell
                    left_cell.right = curr_cell
        repaint(self._first_cell.right, self._first_cell.color)
        repaint(self._first_cell.down, self._first_cell.color)
        last_cell = self._first_cell
        while last_cell.down is not None:
            last_cell = last_cell.down
        while last_cell.right is not None:
            last_cell = last_cell.right
        self.state = RepaintGameState.PLAYING
        while True:
            self.print_field(self._first_cell)
            color = input("Vvodi: ")
            repaint(self._first_cell, color)
            if self.check_win(last_cell):
                self.print_field(self._first_cell)
                print("you won asshole!!212! now kill yourself")
                self.state = RepaintGameState.WIN
                break

    @property
    def row_count(self) -> int:
        return self._row_count

    @property
    def col_count(self) -> int:
        return self._col_count

    @property
    def color_count(self) -> int:
        return self._color_count

    @property
    def first_cell(self) -> Cell:
        return self._first_cell

    @property
    def state(self) -> RepaintGameState:
        return self._state

    @state.setter
    def state(self, a):
        self._state = a

    def print_field(self, cell):
        curr_cell = cell
        down_cell = cell.down
        for i in range(self.row_count):
            for j in range(self.col_count):
                print('{0} '.format(curr_cell.color), end='')
                curr_cell = curr_cell.right
            print()
            curr_cell = down_cell
            if i != self.row_count - 1:
                down_cell = down_cell.down

    def check_win(self, cell):
        if not cell.is_painted:
            return False
        curr_cell = cell
        up_cell = cell.up
        for i in range(self.row_count):
            for j in range(self.col_count):
                if not curr_cell.is_painted:
                    return False
                curr_cell = curr_cell.left
            curr_cell = up_cell
            if i != self.row_count - 1:
                up_cell = up_cell.up
        return True


def repaint(cell, color):
    if cell is None:
        return
    if cell.is_painted and color != cell.color:
        cell.color = color
        repaint(cell.left, color)
        repaint(cell.up, color)
        repaint(cell.right, color)
        repaint(cell.down, color)
        return
    if not cell.is_painted and color == cell.color:
        cell.is_painted = True
        repaint(cell.left, color)
        repaint(cell.up, color)
        repaint(cell.right, color)
        repaint(cell.down, color)
        return


if __name__ == '__main__':
    print(list(colors.keys()))
    game = RepaintGame(12, 12, 6)
