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
        self.__objects = None

    def __get_empty_objects(self) -> list:
        return [SPACE for _ in range(self.__field_size ** 2)]

    def get_center_cell_position(self):
        return self.__field_size//2, self.__field_size//2

    def get_size(self):
        return self.__field_size

    def set_objects(self, objects):
        self.__objects = objects

    def draw(self):
        if not self.__objects:
            self.__objects = self.__get_empty_objects()
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
        print(field.format(*self.__objects))


class GameObject:

    def __init__(self, character=None):
        self.character = character
        self.pos_x = None
        self.pos_y = None

    def set_pos(self, x: int, y: int):
        self.pos_x = x
        self.pos_y = y

    def get_pos(self):
        return self.pos_x, self.pos_y


class FieldObjectFromGameObjectFactory:

    @staticmethod
    def generate(objects: List['GameObject'], field_size: int) -> list:
        field_objects = [SPACE for _ in range(field_size ** 2)]
        for game_object in objects:
            x, y = game_object.get_pos()
            position = (y * field_size) + x
            field_objects.pop(position)
            field_objects.insert(position, game_object.character)
        return field_objects


class Game:

    __slots__ = ['cursor', 'field', 'objects']

    def __init__(self):
        self.field = GameField(3, 7)
        self.cursor = None
        self.objects = []
        self.init_cursor()

    def run(self):
        field_objects = FieldObjectFromGameObjectFactory().generate(
            self.objects, self.field.get_size()
        )
        self.field.set_objects(field_objects)
        self.field.draw()

    def init_cursor(self):
        self.cursor = GameObject(CURSOR)
        center_cell_position = self.field.get_center_cell_position()
        self.cursor.set_pos(*center_cell_position)
        self.objects.append(self.cursor)


if __name__ == '__main__':
    game = Game()
    game.run()
