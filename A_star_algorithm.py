from puzzle import Puzzle


class Node:
    def __init__(self, puzzle):
        self.state = puzzle.state
        self.heuristic_cost = get_heuristic_cost(self.state)
        self.children = get_transition_models(self.state)


def get_heuristic_cost(state):
    cost = 0

    for i in range(3):
        for j in range(3):
            tile_content = state[i][j]

            if tile_content == "1":
                cost += abs(i - 0) + abs(j - 1)
            elif tile_content == "2":
                cost += abs(i - 0) + abs(j - 2)
            elif tile_content == "3":
                cost += abs(i - 1) + abs(j - 0)
            elif tile_content == "4":
                cost += abs(i - 1) + abs(j - 1)
            elif tile_content == "5":
                cost += abs(i - 1) + abs(j - 2)
            elif tile_content == "6":
                cost += abs(i - 2) + abs(j - 0)
            elif tile_content == "7":
                cost += abs(i - 2) + abs(j - 1)
            elif tile_content == "8":
                cost += abs(i - 2) + abs(j - 2)

    return cost


def get_transition_models(state):
    transition_models = []
    trans_state_1 = []
    trans_state_2 = []
    trans_state_3 = []
    trans_state_4 = []

    # 0 is in a corner
    if state[0][0] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[0][1], trans_state_1[0][0] = trans_state_1[0][0], trans_state_1[0][1]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][0], trans_state_2[0][0] = trans_state_2[0][0], trans_state_2[1][0]
    elif state[2][2] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[2][1], trans_state_1[2][2] = trans_state_1[2][2], trans_state_1[2][1]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][2], trans_state_2[2][2] = trans_state_2[2][2], trans_state_2[1][2]
    elif state[0][2] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[0][1], trans_state_1[0][2] = trans_state_1[0][2], trans_state_1[0][1]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][2], trans_state_2[0][2] = trans_state_2[0][2], trans_state_2[1][2]
    elif state[2][0] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[2][1], trans_state_1[2][0] = trans_state_1[2][0], trans_state_1[2][1]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][0], trans_state_2[2][0] = trans_state_2[2][0], trans_state_2[1][0]

    # 0 is on a border
    elif state[1][0] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[0][0], trans_state_1[1][0] = trans_state_1[1][0], trans_state_1[0][0]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][1], trans_state_2[1][0] = trans_state_2[1][0], trans_state_2[1][1]
        trans_state_3 = [row[:] for row in state]
        trans_state_3[2][0], trans_state_3[1][0] = trans_state_3[1][0], trans_state_3[2][0]
    elif state[0][1] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[0][0], trans_state_1[0][1] = trans_state_1[0][1], trans_state_1[0][0]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][1], trans_state_2[0][1] = trans_state_2[0][1], trans_state_2[1][1]
        trans_state_3 = [row[:] for row in state]
        trans_state_3[0][2], trans_state_3[0][1] = trans_state_3[0][1], trans_state_3[0][2]
    elif state[1][2] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[0][2], trans_state_1[1][2] = trans_state_1[1][2], trans_state_1[0][2]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][1], trans_state_2[1][2] = trans_state_2[1][2], trans_state_2[1][1]
        trans_state_3 = [row[:] for row in state]
        trans_state_3[2][2], trans_state_3[1][2] = trans_state_3[1][2], trans_state_3[2][2]
    elif state[2][1] == "0":
        trans_state_1 = [row[:] for row in state]
        trans_state_1[2][0], trans_state_1[2][1] = trans_state_1[2][1], trans_state_1[2][0]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][1], trans_state_2[2][1] = trans_state_2[2][1], trans_state_2[1][1]
        trans_state_3 = [row[:] for row in state]
        trans_state_3[2][2], trans_state_3[2][1] = trans_state_3[2][1], trans_state_3[2][2]

    # 0 is in the center
    else:
        trans_state_1 = [row[:] for row in state]
        trans_state_1[0][1], trans_state_1[1][1] = trans_state_1[1][1], trans_state_1[0][1]
        trans_state_2 = [row[:] for row in state]
        trans_state_2[1][0], trans_state_2[1][1] = trans_state_2[1][1], trans_state_2[1][0]
        trans_state_3 = [row[:] for row in state]
        trans_state_3[2][1], trans_state_3[1][1] = trans_state_3[1][1], trans_state_3[2][1]
        trans_state_4 = [row[:] for row in state]
        trans_state_4[1][2], trans_state_4[1][1] = trans_state_4[1][1], trans_state_4[1][2]

    transition_models.append(trans_state_1)
    transition_models.append(trans_state_2)
    if trans_state_3 != []:
        transition_models.append(trans_state_3)
    if trans_state_4 != []:
        transition_models.append(trans_state_4)

    return transition_models


def solve_puzzle(puzzle, screen):
    goal_state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]
    visited_nodes = []
    frontier = []

    root = Node(puzzle)
    visited_nodes.append(root)

    for child_state in root.children:
        child_as_puzzle = Puzzle(screen)
        child_as_puzzle.set_state(child_state)
        child_node = Node(child_as_puzzle)
        child_node.heuristic_cost += root.heuristic_cost
        frontier.append(child_node)

    trial_no = 1
    while len(frontier) > 0:
        # getting node with the least cost
        min_cost = frontier[0].heuristic_cost
        min_index = 0
        for i in range(len(frontier)):
            if frontier[i].heuristic_cost < min_cost:
                min_cost = frontier[i].heuristic_cost
                min_index = i

        # expanding node with the least heuristic cost
        node_to_expand = frontier.pop(min_index)
        node_in_puzzle_form = Puzzle(screen)
        node_in_puzzle_form.set_state(node_to_expand.state)
        for child_state in node_to_expand.children:
            child_as_puzzle = Puzzle(screen)
            child_as_puzzle.set_state(child_state)
            child_node = Node(child_as_puzzle)
            child_node.heuristic_cost += root.heuristic_cost
            frontier.append(child_node)

        print(f"\nState no: {trial_no}")
        node_in_puzzle_form.print_puzzle()

        if node_to_expand.state == goal_state:
            print("Puzzle solved successfully")
            return

        trial_no += 1
    print("Failed to solve puzzle")
