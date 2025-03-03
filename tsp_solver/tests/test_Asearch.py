# Unit tests for A* Search
import unittest
from tsp_solver.algorithms import Asearch

class TestAStarSearch(unittest.TestCase):
    def setUp(self):
        self.cities = [(0, 0), (2, 3), (5, 4), (6, 1)]

    def test_output_format(self):
        path, cost = Asearch.solve_tsp(self.cities)
        self.assertIsInstance(path, list)
        self.assertIsInstance(cost, float)

    def test_valid_tour(self):
        path, _ = Asearch.solve_tsp(self.cities)
        self.assertEqual(len(set(path[:-1])), len(self.cities))  # All cities must be visited once
        self.assertEqual(path[0], path[-1])  # Must return to start

if __name__ == "__main__":
    unittest.main()
