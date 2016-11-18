
import unittest
from conway import ConwaysGame
import numpy

class TestInit(unittest.TestCase):

    def test_init_empty(self):
        "__init__ should return empty board "
        game = ConwaysGame(shape=[10,10])
        self.assertEqual(game.live_cells_count(), 0)

    def test_init_data(self):
        "__init__ with params should copy the board"
        data = numpy.zeros(shape=[9,9])
        data[2][2] = data[1][2] = data[2][1] = True
        game = ConwaysGame(data=data)
        self.assertEqual(game.live_cells_count(), 3)

    def test_random_fill(self):
        "add_random_cells should add some cells"
        game = ConwaysGame(shape=[10,10])
        self.assertEqual(game.live_cells_count(), 0)
        game.add_random_cells()
        self.assertNotEqual(game.live_cells_count(), 0)

    def test_parametrized_fill(self):
        "add_random_cells(20) should add 20 cells"
        game = ConwaysGame(shape=[10,10])
        self.assertEqual(game.live_cells_count(), 0)
        game.add_random_cells(count=20)
        self.assertNotEqual(game.live_cells_count(), 20)

class TestSteps(unittest.TestCase):
    def test_pulsar(self):
        "Test pulsar"
        data = numpy.zeros(shape=[9,9])
        data[2][2] = data[1][2] = data[2][1] = True
        game = ConwaysGame(data=data)
        self.assertEqual(game.live_cells_count(), 3)
        game.next_step()
        self.assertEqual(game.live_cells_count(), 3)
