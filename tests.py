import io
import sys
from unittest import TestCase

from main import Game, GameField


class TestGame(TestCase):

    def setUp(self) -> None:
        self.game = Game()

    def test__move_cursor(self):

        self.assertTupleEqual((1, 1), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(1, 0))
        self.assertTupleEqual((2, 1), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(1, 0))
        self.assertTupleEqual((0, 1), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(-1, 0))
        self.assertTupleEqual((2, 1), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(-1, 0))
        self.assertTupleEqual((1, 1), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(0, 1))
        self.assertTupleEqual((1, 2), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(0, 1))
        self.assertTupleEqual((1, 0), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(0, -1))
        self.assertTupleEqual((1, 2), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(0, -1))
        self.assertTupleEqual((1, 1), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(1, 1))
        self.assertTupleEqual((2, 2), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(1, 1))
        self.assertTupleEqual((0, 0), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(-1, -1))
        self.assertTupleEqual((2, 2), self.game.cursor.get_pos())

        self.game.move_cursor(direction=(-1, -1))
        self.assertTupleEqual((1, 1), self.game.cursor.get_pos())

    def tearDown(self) -> None:
        pass


class TestGameField(TestCase):

    def setUp(self) -> None:
        self.field = GameField()

    def test__draw(self):
        reference_data = \
            f'┌───┬───┬───┐\n' \
            f'│   │   │   │\n' \
            f'├───┼───┼───┤\n' \
            f'│   │   │   │\n' \
            f'├───┼───┼───┤\n' \
            f'│   │   │   │\n' \
            f'└───┴───┴───┘\n'
        output = io.StringIO()
        sys.stdout = output
        self.field.draw()
        self.assertEqual(reference_data, output.getvalue())

    def tearDown(self) -> None:
        pass
