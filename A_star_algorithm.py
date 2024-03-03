from puzzle import Puzzle


class Node:
    def __init__(self, puzzle, parent):
        self.state = puzzle.state
        self.heuristic_cost = get_heuristic_cost(self.state)
        self.children = get_transition_models(self.state)
        self.parent = parent


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


def get_visited_nodes_states(visited_nodes):
    states = []
    for i in range(len(visited_nodes)):
        states.append(visited_nodes[i].state)
    return states


def get_path_to_goal(node):
    path = []  # path from end to start
    while node is not None:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # reversed to get correct sequence from start to end


def solve_puzzle(puzzle):
    goal_state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]
    visited_nodes = []
    frontier = []

    root = Node(puzzle, None)
    visited_nodes.append(root)
    if root.state == goal_state:
        return get_path_to_goal(root)

    for child_state in root.children:
        child_as_puzzle = Puzzle()
        child_as_puzzle.set_state(child_state)
        child_node = Node(child_as_puzzle, root)
        child_node.heuristic_cost += root.heuristic_cost
        frontier.append(child_node)

    trial_no = 1
    while len(frontier) > 0:
        """
        print("frontier: ")
        for obj in frontier:
            print(obj.state)
            print(obj.heuristic_cost)
        """

        # getting node with the least cost
        min_cost = frontier[0].heuristic_cost
        min_index = 0
        for i in range(len(frontier)):
            if frontier[i].heuristic_cost < min_cost:
                min_cost = frontier[i].heuristic_cost
                min_index = i

        # expanding node with the least heuristic cost
        node_to_expand = frontier.pop(min_index)
        visited_nodes.append(node_to_expand)
        node_in_puzzle_form = Puzzle()
        node_in_puzzle_form.set_state(node_to_expand.state)
        for child_state in node_to_expand.children:
            child_as_puzzle = Puzzle()
            child_as_puzzle.set_state(child_state)
            child_node = Node(child_as_puzzle, node_to_expand)
            child_node.heuristic_cost += root.heuristic_cost

            exists_in_frontier_or_visited = False
            for node in frontier:
                if node.state == child_state:
                    exists_in_frontier_or_visited = True
                    break

            for node in visited_nodes:
                if node.state == child_state:
                    exists_in_frontier_or_visited = True
                    break

            if not exists_in_frontier_or_visited:
                frontier.append(child_node)

        print(f"\nExplored State no: {trial_no}")
        node_in_puzzle_form.print_puzzle()

        if node_to_expand.state == goal_state:
            print("Puzzle solved successfully")
            # return get_visited_nodes_states(visited_nodes)
            return get_path_to_goal(node_to_expand)

        trial_no += 1
    print("Failed to solve puzzle")
