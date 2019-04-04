import unittest
import time
from GameOfLife import Neighbour_Counts
from GameOfLife import New_State
from GameOfLife import print_grid
from GameOfLife import isGameOver
from GameOfLife import read_grid
from os import system

class TestNeighbours(unittest.TestCase):
    def test_no_alive_neighbours(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        actualNeighbourCounts = Neighbour_Counts(grid, 1, 1)
        self.assertEqual(actualNeighbourCounts, 0)
    
    def test_wrapping(self):
        grid = [
            [0, 0, 1],
            [0, 0, 0],
            [1, 0, 0]
        ]
        actualNeighbourCounts = Neighbour_Counts(grid, 0, 0)
        self.assertEqual(actualNeighbourCounts, 2)

    def test_cell_death(self):
        grid = [
            [1,1,1],
            [1,1,1],
            [1,1,1]
        ]
        cellDeath = isGameOver(grid)
        self.assertFalse(cellDeath)

    def test_cell_death_true(self):
        grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        cellDeath = isGameOver(grid)
        self.assertTrue(cellDeath)

    def test_cell_death_mix(self):
        grid = [
            [0,0,0],
            [0,0,0],
            [1,1,1]
        ]
        cellDeath = isGameOver(grid)
        self.assertFalse(cellDeath)

    def test_conway_rule_1(self):
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        newState = New_State(grid)
        expectedNewState = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(newState, expectedNewState)

    def test_conway_rule_2(self):
        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        newState = New_State(grid)
        expectedNewState = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(newState, expectedNewState)

    def test_conway_rule_3(self):
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        newState = New_State(grid)
        expectedNewState = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(newState, expectedNewState)

    def test_conway_rule_4(self):
        grid = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]
        newState = New_State(grid)
        expectedNewState = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 1, 1]
        ]
        self.assertEqual(newState, expectedNewState)

    def test_conway_rule_5(self):
        grid = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 1]
        ]
        newState = New_State(grid)
        expectedNewState = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(newState, expectedNewState)
    
if __name__ == '__main__':
    unittest.main()