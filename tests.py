from unittest import TestCase

from main import Game


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