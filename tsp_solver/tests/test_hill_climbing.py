# Unit tests for Hill Climbing
import unittest
from tsp_solver.algorithms import hill_climbing

class TestHillClimbing(unittest.TestCase):
    def setUp(self):
        self.cities = [(0, 0), (2, 3), (5, 4), (6, 1)]

    def test_output_format(self):
        path, cost = hill_climbing.solve_tsp(self.cities)
        self.assertIsInstance(path, list)
        self.assertIsInstance(cost, float)

    def test_valid_tour(self):
        path, _ = hill_climbing.solve_tsp(self.cities)
        self.assertEqual(len(set(path[:-1])), len(self.cities))
        self.assertEqual(path[0], path[-1])

if __name__ == "__main__":
    unittest.main()
