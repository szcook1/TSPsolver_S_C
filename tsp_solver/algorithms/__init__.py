from .Asearch import solve_tsp as astar
from .random_search import solve_tsp as random_search
from .hill_climbing import solve_tsp as hill_climbing
from .simulated_annealing import solve_tsp as simulated_annealing

__all__ = ["astar", "random_search", "hill_climbing", "simulated_annealing"]
