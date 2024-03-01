import random
import tkinter as tk

class Puzzle:
    def __init__(self, screen):
        self.state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
        ]
        self.canvas = tk.Canvas(screen, width=500, height=500)

    def print_puzzle(self):
        for i in range(3):
            row = "|"
            for j in range(3):
                row += self.state[i][j] + "|"
            print(row)

    def show_puzzle_on_screen(self):
        self.canvas.pack()
        self.create_layout()

    def set_state(self, state):
        self.state = state

    def shuffle_puzzle(self):
        flag = False

        for n in range(10):
            for i in range(3):
                for j in range(3):
                    if self.state[i][j] == "0":

                        # 0 is in a corner
                        if i == 0 and j == 0:  # 0 at upper left corner
                            random_number = random.randint(0, 1)
                            if random_number == 0:
                                self.state[i][j + 1], self.state[i][j] = self.state[i][j], self.state[i][j + 1]
                            else:
                                self.state[i + 1][j], self.state[i][j] = self.state[i][j], self.state[i + 1][j]
                        elif i == 2 and j == 2:  # 0 at lower right corner
                            random_number = random.randint(0, 1)
                            if random_number == 0:
                                self.state[i][j - 1], self.state[i][j] = self.state[i][j], self.state[i][j - 1]
                            else:
                                self.state[i - 1][j], self.state[i][j] = self.state[i][j], self.state[i - 1][j]
                        elif i == 0 and j == 2:  # 0 at upper right corner
                            random_number = random.randint(0, 1)
                            if random_number == 0:
                                self.state[i][j - 1], self.state[i][j] = self.state[i][j], self.state[i][j - 1]
                            else:
                                self.state[i + 1][j], self.state[i][j] = self.state[i][j], self.state[i + 1][j]
                        elif i == 2 and j == 0:  # 0 at lower left corner
                            random_number = random.randint(0, 1)
                            if random_number == 0:
                                self.state[i][j + 1], self.state[i][j] = self.state[i][j], self.state[i][j + 1]
                            else:
                                self.state[i - 1][j], self.state[i][j] = self.state[i][j], self.state[i - 1][j]

                        # 0 is on a border
                        elif i == 1 and j == 0:
                            random_number = random.randint(0, 2)
                            if random_number == 0:
                                self.state[i - 1][j], self.state[i][j] = self.state[i][j], self.state[i - 1][j]
                            elif random_number == 1:
                                self.state[i][j + 1], self.state[i][j] = self.state[i][j], self.state[i][j + 1]
                            else:
                                self.state[i + 1][j], self.state[i][j] = self.state[i][j], self.state[i + 1][j]
                        elif i == 0 and j == 1:
                            random_number = random.randint(0, 2)
                            if random_number == 0:
                                self.state[i][j - 1], self.state[i][j] = self.state[i][j], self.state[i][j - 1]
                            elif random_number == 1:
                                self.state[i + 1][j], self.state[i][j] = self.state[i][j], self.state[i + 1][j]
                            else:
                                self.state[i][j + 1], self.state[i][j] = self.state[i][j], self.state[i][j + 1]
                        elif i == 1 and j == 2:
                            random_number = random.randint(0, 2)
                            if random_number == 0:
                                self.state[i - 1][j], self.state[i][j] = self.state[i][j], self.state[i - 1][j]
                            elif random_number == 1:
                                self.state[i][j - 1], self.state[i][j] = self.state[i][j], self.state[i][j - 1]
                            else:
                                self.state[i + 1][j], self.state[i][j] = self.state[i][j], self.state[i + 1][j]
                        elif i == 2 and j == 1:
                            random_number = random.randint(0, 2)
                            if random_number == 0:
                                self.state[i][j - 1], self.state[i][j] = self.state[i][j], self.state[i][j - 1]
                            elif random_number == 1:
                                self.state[i - 1][j], self.state[i][j] = self.state[i][j], self.state[i - 1][j]
                            else:
                                self.state[i][j + 1], self.state[i][j] = self.state[i][j], self.state[i][j + 1]

                        # 0 is in the center
                        else:
                            random_number = random.randint(0, 3)
                            if random_number == 0:
                                self.state[i][j - 1], self.state[i][j] = self.state[i][j], self.state[i][j - 1]
                            elif random_number == 1:
                                self.state[i - 1][j], self.state[i][j] = self.state[i][j], self.state[i - 1][j]
                            elif random_number == 2:
                                self.state[i + 1][j], self.state[i][j] = self.state[i][j], self.state[i + 1][j]
                            else:
                                self.state[i][j + 1], self.state[i][j] = self.state[i][j], self.state[i][j + 1]

                        flag = True
                        break

                if flag:
                    flag = False
                    break

    def create_tile(self, x, y, width, radius, height, number):
        # Create the outer border
        x1 = x
        x2 = x + width
        y1 = y
        y2 = y1 + width
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]

        kwargs = {
            "fill": "DarkOrange2"
        }
        self.canvas.create_polygon(points, **kwargs, smooth=True)
        # canvas.create_rectangle(x, y, x+width, y+height, outline="black", width=4, fill="DarkOrange4")
        # Insert the number
        text_x = x + width / 2
        text_y = y + height / 2
        self.canvas.create_text(text_x, text_y, text=str(number), font=("Helvetica", 35, "bold"), fill="black")

    def create_layout(self):
        container_x = 80
        container_y = 80
        container_width = 430
        container_height = 430
        self.canvas.create_rectangle(container_x, container_y, container_width, container_height,
                                     outline="black", width=6, fill="DarkOrange4")

        # Create the bordered tiles
        tile_x = 100
        tile_y = 100
        for i in range(3):
            for j in range(3):
                tile_width = 100
                tile_height = 100
                tile_radius = 30
                self.create_tile(tile_x, tile_y, tile_width, tile_radius, tile_height, self.state[i][j])
                tile_x += 105
            tile_x = 100
            tile_y += 105
