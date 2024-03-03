from A_star_algorithm import solve_puzzle
from puzzle import Puzzle
from gui import GUI

p = Puzzle()
p.shuffle_puzzle()

print("Original state")
p.set_state(
    [
        ["3", "1", "2"],
        ["0", "4", "7"],
        ["6", "8", "5"],
    ]
)

p.print_puzzle()

path_to_goal = solve_puzzle(p)
print("path:")
print(path_to_goal)

gui = GUI(A_star_path=path_to_goal)
gui.show_puzzle_on_screen()
