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
DUMMY = " "

DEFAULT_CELL_SIZE = 1
DEFAULT_FIELD_SIZE = 3


class GameField:

    def __init__(self, cell_size: int = DEFAULT_CELL_SIZE, field_size: int = DEFAULT_FIELD_SIZE):
        self.__sign = None
        self.__cells = None
        self.__cell_size = cell_size  # TODO: Organize descriptor
        self.__field_size = field_size

    def draw(self):
        top_line = f'{LEFT_TOP}{HORIZONTAL * self.__cell_size}' + \
                   f'{TOP_BETWEEN}{HORIZONTAL * self.__cell_size}' * (self.__field_size - 1) + \
                   f'{RIGHT_TOP}'
        horizontal_cell_size = int(self.__cell_size / 3) if self.__cell_size >= 3 else 1
        between_vertical = '\n'.join(
            [
                f'{VERTICAL}{DUMMY * self.__cell_size}' * (self.__field_size + 1)
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
        print(field)


if __name__ == '__main__':
    game_field = GameField(3, 3)
    game_field.draw()
