import pygame
import tkinter as tk
from tkinter import ttk


def state_button_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/camera_shutter_state_button.mp3")  # Replace "sound_effect.wav" with your sound file
    pygame.mixer.music.play()


def algo_select_button_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("assets/algo_select_pan_hit.mp3")  # Replace "sound_effect.wav" with your sound file
    pygame.mixer.music.play()


def initial_state_validate(d, i, P, s, S, v, V, W):
    return len(P) <= 9


class GUI:
    def __init__(self, A_star_path):
        self.screen = tk.Tk()
        self.screen.title("8 Puzzle")
        self.canvas = tk.Canvas(self.screen, width=800, height=500)
        self.A_star_states = A_star_path
        self.current_state = 1
        self.selected_strategy = ""

    def show_puzzle_on_screen(self):
        self.canvas.pack()
        self.create_layout()
        self.screen.mainloop()

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
            "fill": "MediumPurple1"
        }
        self.canvas.create_polygon(points, **kwargs, smooth=True)
        # Insert the number
        text_x = x + width / 2
        text_y = y + height / 2
        self.canvas.create_text(text_x, text_y, text=str(number), font=("Helvetica", 35, "bold"), fill="black")

    def back_button_command(self):
        state_button_sound()
        if self.current_state != 1:
            self.current_state -= 1
            self.canvas.delete("all")
            self.create_layout()

    def forward_button_command(self):
        state_button_sound()
        if self.current_state != len(self.A_star_states):
            self.current_state += 1
            self.canvas.delete("all")
            self.create_layout()

    def bfs_button_command(self):
        algo_select_button_sound()
        self.selected_strategy = "bfs"
        self.current_state = 1
        self.canvas.delete("all")
        self.create_layout()

    def dfs_button_command(self):
        algo_select_button_sound()
        self.selected_strategy = "dfs"
        self.current_state = 1
        self.canvas.delete("all")
        self.create_layout()

    def a_star_button_command(self):
        algo_select_button_sound()
        self.selected_strategy = "A*"
        self.current_state = 1
        self.canvas.delete("all")
        self.create_layout()

    def create_layout(self):
        # Create initial state input area
        initial_state_input_label_x = 200
        initial_state_input_label_y = 40
        initial_state_input_label_text = "Enter Initial Puzzle State:"
        initial_state_input_label = tk.Label(self.screen, text=initial_state_input_label_text, font=("Helvetica", 14, "bold"))
        selected_strategy_label_window = self.canvas.create_window(initial_state_input_label_x, initial_state_input_label_y, window=initial_state_input_label)

        initial_state_entry_x = 375
        initial_state_entry_y = 40
        validate_cmd = self.screen.register(initial_state_validate)
        initial_state_entry = ttk.Entry(self.screen, width=10, font=("Helvetica", 14, "bold"), validate="key", validatecommand=(validate_cmd, '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W'))
        initial_state_entry_window = self.canvas.create_window(initial_state_entry_x, initial_state_entry_y, window=initial_state_entry)

        create_button_x = 530
        create_button_y = 40
        create_button_width = 13
        create_button_height = 2
        create_button = tk.Button(self.screen, text="Create Puzzle", font=("Helvetica", 12, "bold"), width=create_button_width, height=create_button_height, activebackground="CadetBlue3", background="CadetBlue1", borderwidth=2)
        self.canvas.create_window(create_button_x, create_button_y, window=create_button)

        random_button_x = 692
        random_button_y = 40
        random_button_width = 13
        random_button_height = 2
        random_button = tk.Button(self.screen, text="Random Puzzle", font=("Helvetica", 12, "bold"), width=random_button_width, height=random_button_height, activebackground="turquoise3", background="turquoise1", borderwidth=2)
        self.canvas.create_window(random_button_x, random_button_y, window=random_button)

        # Create main puzzle container
        container_x = 80
        container_y = 80
        container_width = 430
        container_height = 430
        self.canvas.create_rectangle(container_x, container_y, container_width, container_height, outline="purple1", width=6, fill="purple4")

        # Create the bordered tiles
        tile_x = 100
        tile_y = 100
        for i in range(3):
            for j in range(3):
                tile_width = 100
                tile_height = 100
                tile_radius = 30
                if self.A_star_states[self.current_state - 1][i][j] != "0":
                    if self.selected_strategy == "A*":
                        self.create_tile(tile_x, tile_y, tile_width, tile_radius, tile_height, self.A_star_states[self.current_state - 1][i][j])
                    else:
                        self.create_tile(tile_x, tile_y, tile_width, tile_radius, tile_height, self.A_star_states[0][i][j])

                tile_x += 105
            tile_x = 100
            tile_y += 105

        # Create algorithm selection section
        algo_container_x = 460
        algo_container_y = 80
        algo_container_width = 300
        algo_container_height = 270
        self.canvas.create_rectangle(algo_container_x, algo_container_y, algo_container_x + algo_container_width, algo_container_y + algo_container_height, outline="black", width=2)
        algo_title_label_text = "Select a solving strategy"
        algo_title_label = tk.Label(self.screen, text=algo_title_label_text, font=("Helvetica", 18, "bold"))
        algo_title_label_window = self.canvas.create_window(algo_container_x + algo_container_width / 2, algo_container_y + 20, window=algo_title_label)

        bfs_button_x = 610
        bfs_button_y = 150
        bfs_button_width = 20
        bfs_button_height = 2
        bfs_button = tk.Button(self.screen, text="Breadth First Search", font=("Helvetica", 12, "bold"), width=bfs_button_width, height=bfs_button_height, activebackground="MediumOrchid3", background="MediumOrchid1", borderwidth=2, command=self.bfs_button_command)
        self.canvas.create_window(bfs_button_x, bfs_button_y, window=bfs_button)

        dfs_button_x = 610
        dfs_button_y = 220
        dfs_button_width = 20
        dfs_button_height = 2
        dfs_button = tk.Button(self.screen, text="Depth First Search", font=("Helvetica", 12, "bold"), width=dfs_button_width, height=dfs_button_height, activebackground="DarkOrchid3", background="DarkOrchid1", borderwidth=2, command=self.dfs_button_command)
        self.canvas.create_window(dfs_button_x, dfs_button_y, window=dfs_button)

        a_star_button_x = 610
        a_star_button_y = 290
        a_star_button_width = 20
        a_star_button_height = 2
        a_star_button = tk.Button(self.screen, text="A* Algorithm", font=("Helvetica", 12, "bold"), width=a_star_button_width, height=a_star_button_height, activebackground="purple3", background="purple1", borderwidth=2, command=self.a_star_button_command)
        self.canvas.create_window(a_star_button_x, a_star_button_y, window=a_star_button)

        # Create buttons
        if self.selected_strategy == "A*":
            back_button_x = 500
            back_button_y = 400
            back_arrow_image = tk.PhotoImage(file="assets/back_arrow.png")
            back_button = tk.Button(self.screen, image=back_arrow_image, borderwidth=0, command=self.back_button_command)
            back_button.image = back_arrow_image  # Keep a reference to the image to prevent garbage collection
            self.canvas.create_window(back_button_x, back_button_y, window=back_button)

            back_button_x = 720
            back_button_y = 400
            back_arrow_image = tk.PhotoImage(file="assets/forward_arrow.png")
            back_button = tk.Button(self.screen, image=back_arrow_image, borderwidth=0, command=self.forward_button_command)
            back_button.image = back_arrow_image  # Keep a reference to the image to prevent garbage collection
            self.canvas.create_window(back_button_x, back_button_y, window=back_button)

            # Create state number label
            label_x = 540
            label_y = 360
            label_width = 140
            label_height = 80
            self.canvas.create_rectangle(label_x, label_y, label_x + label_width, label_y + label_height, outline="black", width=2)

            if self.selected_strategy == "A*":
                states_limit = len(self.A_star_states)
            else:
                states_limit = 0

            label_text = f"{self.current_state} / {states_limit}"
            label = tk.Label(self.screen, text=label_text, font=("Helvetica", 18, "bold"))
            label_window = self.canvas.create_window(label_x + label_width / 2, label_y + label_height / 2, window=label)

            selected_strategy_label_x = 610
            selected_strategy_label_y = 470
            selected_strategy_label_text = f"Selected Strategy: {self.selected_strategy}"
            selected_strategy_label = tk.Label(self.screen, text=selected_strategy_label_text, font=("Helvetica", 14, "bold"))
            selected_strategy_label_window = self.canvas.create_window(selected_strategy_label_x, selected_strategy_label_y, window=selected_strategy_label)
