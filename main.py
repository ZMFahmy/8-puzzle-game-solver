from A_star_algorithm import solve_puzzle
from puzzle import Puzzle
from gui import GUI

p = Puzzle()
p.shuffle_puzzle()

print("Original state")
p.print_puzzle()
state=[["4","3","1"],
       ["5","0","2"],
       ["6","7","8"]]
p.set_state(state)

visited_nodes = solve_puzzle(p)

gui = GUI(A_star_states=visited_nodes)
gui.show_puzzle_on_screen()
