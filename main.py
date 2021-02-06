from typing import List

LEFT_BETWEEN = "├"
LEFT_TOP = "┌"
LEFT_BOTTOM = "└"
RIGHT_BETWEEN = "┤"
RIGHT_TOP = "┐"
RIGHT_BOTTOM = "┘"
TOP_BETWEEN = "┬"
BOTTOM_BETWEEN = "┴"
BETWEEN_BETWEEN = "┼"
HORIZONTAL = "─"
VERTICAL = "│"
DUMMY = "{}"
SPACE = " "

TIC = "X"
TOE = "O"

CURSOR = "█"

DEFAULT_CELL_SIZE = 3
DEFAULT_FIELD_SIZE = 3


class GameField:

    def __init__(self, cell_size: int = DEFAULT_CELL_SIZE, field_size: int = DEFAULT_FIELD_SIZE):
        self.__sign = None
        self.__cells = None
        self.__cell_size = cell_size  # TODO: Organize descriptor
        self.__field_size = field_size

    def __get_empty_objects(self) -> list:
        return [SPACE for _ in range(self.__field_size ** 2)]

    def draw(self, objects: list = None):
        if not objects:
            objects = self.__get_empty_objects()
        top_line = f'{LEFT_TOP}{HORIZONTAL * self.__cell_size}' + \
                   f'{TOP_BETWEEN}{HORIZONTAL * self.__cell_size}' * (self.__field_size - 1) + \
                   f'{RIGHT_TOP}'
        horizontal_cell_size = int(self.__cell_size / 3) if self.__cell_size >= 3 else 1
        between_vertical = '\n'.join(
            [
                f'{VERTICAL}{DUMMY.center(self.__cell_size+1, SPACE)}' * self.__field_size +
                f'{VERTICAL}'
            ] * horizontal_cell_size
        )
        between_horizontal = f'{LEFT_BETWEEN}{HORIZONTAL * self.__cell_size}' + \
                             f'{BETWEEN_BETWEEN}{HORIZONTAL * self.__cell_size}' * (
                                     self.__field_size - 1) + \
                             f'{RIGHT_BETWEEN}'

        between_cells = '\n'.join([between_vertical, between_horizontal] * (self.__field_size - 1))

        bottom_line = f'{LEFT_BOTTOM}{HORIZONTAL * self.__cell_size}' + \
                      f'{BOTTOM_BETWEEN}{HORIZONTAL * self.__cell_size}' * (self.__field_size - 1) + \
                      f'{RIGHT_BOTTOM}'
        field = "\n".join([top_line, between_cells, between_vertical, bottom_line])
        print(field.format(*objects))


class Game:

    def __init__(self):
        self.field = GameField()

    def run(self):
        self.field.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
