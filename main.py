from puzzle import Puzzle
from gui import GUI

p = Puzzle()
p.shuffle_puzzle()

print("Original state")
p.print_puzzle()


gui = GUI()
gui.show_puzzle_on_screen()
