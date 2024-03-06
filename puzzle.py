import random


class Puzzle:
    def __init__(self):
        self.state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
        ]

    def print_puzzle(self):
        for i in range(3):
            row = "|"
            for j in range(3):
                row += self.state[i][j] + "|"
            print(row)

    def set_state(self, state):
        self.state = state

    def shuffle_puzzle(self):
        flag = False

        for n in range(50):
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
