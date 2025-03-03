# Unit tests for Random Search
import unittest
from tsp_solver.algorithms import random_search

class TestRandomSearch(unittest.TestCase):
    def setUp(self):
        self.cities = [(0, 0), (2, 3), (5, 4), (6, 1)]

    def test_output_format(self):
        path, cost = random_search.solve_tsp(self.cities, iterations=100)
        self.assertIsInstance(path, list)
        self.assertIsInstance(cost, float)

    def test_valid_tour(self):
        path, _ = random_search.solve_tsp(self.cities, iterations=100)
        self.assertEqual(len(set(path[:-1])), len(self.cities))
        self.assertEqual(path[0], path[-1])

if __name__ == "__main__":
    unittest.main()
