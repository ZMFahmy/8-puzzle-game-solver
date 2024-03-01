from A_star_algorithm import solve_puzzle
from puzzle import Puzzle
import tkinter as tk

screen = tk.Tk()
screen.title("Bordered Tile")

p = Puzzle(screen)
p.shuffle_puzzle()

print("Original state")
p.print_puzzle()
p.show_puzzle_on_screen()

solve_puzzle(p, screen)
screen.mainloop()
