from typing import List

from settings import (
    BETWEEN_BETWEEN, BOTTOM_BETWEEN, CURSOR, DEFAULT_CELL_SIZE, DEFAULT_FIELD_SIZE, DUMMY,
    HORIZONTAL,
    LEFT_BETWEEN,
    LEFT_BOTTOM, LEFT_TOP, RIGHT_BETWEEN, RIGHT_BOTTOM, RIGHT_TOP,
    SPACE,
    TOP_BETWEEN, VERTICAL,
)


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
                f'{VERTICAL}{DUMMY.center(self.__cell_size + 1, SPACE)}' * self.__field_size +
                f'{VERTICAL}'
            ] * horizontal_cell_size
        )
        between_horizontal = f'{LEFT_BETWEEN}{HORIZONTAL * self.__cell_size}' + \
                             f'{BETWEEN_BETWEEN}{HORIZONTAL * self.__cell_size}' * (
                                     self.__field_size - 1) + \
                             f'{RIGHT_BETWEEN}'

        between_cells = '\n'.join([between_vertical, between_horizontal] * (self.__field_size - 1))

        bottom_line = f'{LEFT_BOTTOM}{HORIZONTAL * self.__cell_size}' + \
                      f'{BOTTOM_BETWEEN}{HORIZONTAL * self.__cell_size}' * \
                      (self.__field_size - 1) + \
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


class Game:

    __slots__ = ['cursor', 'field', 'objects']

    def __init__(self):
        self.field = GameField(3, 3)
        self.cursor = None
        self.objects = []
        self.init_cursor()

    def run(self) -> None:
        field_objects = FieldObjectFromGameObjectFactory().generate(
            self.objects, self.field.get_size()
        )
        self.field.set_objects(field_objects)
        self.field.draw()

    def init_cursor(self) -> None:
        self.cursor = GameObject(CURSOR)
        center_cell_position = self.field.get_center_cell_position()
        self.cursor.set_pos(*center_cell_position)
        self.objects.append(self.cursor)

    def move_cursor(self, direction: tuple) -> None:
        x_max_pos = self.field.get_size() - 1
        y_max_pos = x_max_pos
        x, y = self.cursor.get_pos()
        new_x, new_y = x, y
        if direction == (1, 0):
            new_x = x + 1
        elif direction == (-1, 0):
            new_x = x - 1
        elif direction == (0, 1):
            new_y = y + 1
        elif direction == (0, -1):
            new_y = y - 1
        elif direction == (1, 1):
            new_x = x + 1
            new_y = y + 1
        elif direction == (-1, -1):
            new_x = x - 1
            new_y = y - 1
        else:
            new_x = x
            new_y = y

        if new_x > x_max_pos:
            new_x = 0
        elif new_x < 0:
            new_x = x_max_pos

        if new_y > y_max_pos:
            new_y = 0
        elif new_y < 0:
            new_y = y_max_pos

        self.cursor.set_pos(new_x, new_y)


if __name__ == '__main__':
    game = Game()
    game.run()
