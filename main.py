from A_star_algorithm import solve_puzzle
from puzzle import Puzzle
from gui import GUI

p = Puzzle()
p.shuffle_puzzle()

print("Original state")
p.print_puzzle()

visited_nodes = solve_puzzle(p)

gui = GUI(A_star_states=visited_nodes)
gui.show_puzzle_on_screen()
