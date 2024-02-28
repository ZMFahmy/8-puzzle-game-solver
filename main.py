from A_star_algorithm import solve_puzzle
from puzzle import Puzzle

p = Puzzle()
p.shuffle_puzzle()

print("Original state")
p.print_puzzle()

solve_puzzle(p)
