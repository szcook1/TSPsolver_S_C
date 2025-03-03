# Unit tests for Simulated Annealing
import unittest
from tsp_solver.algorithms import simulated_annealing

class TestSimulatedAnnealing(unittest.TestCase):
    def setUp(self):
        self.cities = [(0, 0), (2, 3), (5, 4), (6, 1)]

    def test_output_format(self):
        path, cost = simulated_annealing.solve_tsp(self.cities, temp=1000, cooling_rate=0.995)
        self.assertIsInstance(path, list)
        self.assertIsInstance(cost, float)

    def test_valid_tour(self):
        path, _ = simulated_annealing.solve_tsp(self.cities, temp=1000, cooling_rate=0.995)
        self.assertEqual(len(set(path[:-1])), len(self.cities))
        self.assertEqual(path[0], path[-1])

if __name__ == "__main__":
    unittest.main()
