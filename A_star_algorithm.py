import math

from puzzle import Puzzle


class Node:
    def __init__(self, puzzle, parent, cost_to_reach_node, metric_type):
        self.state = puzzle.state
        self.cost_to_reach_node = cost_to_reach_node
        self.heuristic_cost = get_heuristic_cost(self.state, metric_type)
        self.children = get_transition_models(self.state)
        self.parent = parent


def get_heuristic_cost(state, metric_type):
    cost = 0

    if metric_type == "Manhattan":
        for i in range(3):
            for j in range(3):
                tile_content = state[i][j]

                if tile_content == "0":
                    cost += abs(i - 0) + abs(j - 0)
                elif tile_content == "1":
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
    else:
        for i in range(3):
            for j in range(3):
                tile_content = state[i][j]

                if tile_content == "0":
                    cost += math.sqrt((i - 0)**2 + (j - 0)**2)
                elif tile_content == "1":
                    cost += math.sqrt((i - 0)**2 + (j - 1)**2)
                elif tile_content == "2":
                    cost += math.sqrt((i - 0)**2 + (j - 2)**2)
                elif tile_content == "3":
                    cost += math.sqrt((i - 1)**2 + (j - 0)**2)
                elif tile_content == "4":
                    cost += math.sqrt((i - 1)**2 + (j - 1)**2)
                elif tile_content == "5":
                    cost += math.sqrt((i - 1)**2 + (j - 2)**2)
                elif tile_content == "6":
                    cost += math.sqrt((i - 2)**2 + (j - 0)**2)
                elif tile_content == "7":
                    cost += math.sqrt((i - 2)**2 + (j - 1)**2)
                elif tile_content == "8":
                    cost += math.sqrt((i - 2)**2 + (j - 2)**2)


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


def solve_puzzle_A_star(puzzle, metric_type):
    goal_state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]
    visited_nodes = []
    frontier = []

    root = Node(puzzle, None, 0, metric_type)
    visited_nodes.append(root)
    if root.state == goal_state:
        return get_path_to_goal(root)

    for child_state in root.children:
        child_as_puzzle = Puzzle()
        child_as_puzzle.set_state(child_state)
        child_node = Node(child_as_puzzle, root, root.cost_to_reach_node + 1, metric_type)
        child_node.heuristic_cost += root.heuristic_cost
        frontier.append(child_node)

    trial_no = 1
    while len(frontier) > 0:
        # getting node with the least cost
        min_cost = frontier[0].heuristic_cost + frontier[0].cost_to_reach_node
        min_index = 0
        for i in range(len(frontier)):
            if frontier[i].heuristic_cost + frontier[i].cost_to_reach_node < min_cost:
                min_cost = frontier[i].heuristic_cost + frontier[i].cost_to_reach_node
                min_index = i

        # expanding node with the least heuristic cost
        node_to_expand = frontier.pop(min_index)
        visited_nodes.append(node_to_expand)
        node_in_puzzle_form = Puzzle()
        node_in_puzzle_form.set_state(node_to_expand.state)
        for child_state in node_to_expand.children:
            child_as_puzzle = Puzzle()
            child_as_puzzle.set_state(child_state)
            child_node = Node(child_as_puzzle, node_to_expand, node_to_expand.cost_to_reach_node + 1, metric_type)

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
            print("Puzzle solved successfully with A*")
            # return get_visited_nodes_states(visited_nodes)
            return get_path_to_goal(node_to_expand)

        trial_no += 1
    print("Failed to solve puzzle with A*")
