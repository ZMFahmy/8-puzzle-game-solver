import math
from puzzle import Puzzle
from heapq import heappush, heappop
import time


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

                #if tile_content == "0":
                #    cost += abs(i - 0) + abs(j - 0)
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
    else:
        for i in range(3):
            for j in range(3):
                tile_content = state[i][j]

                #if tile_content == "0":
                #   cost += math.sqrt((i - 0)**2 + (j - 0)**2)
                if tile_content == "1":
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


def state_to_string(puzzle_state):
    state_string = ""
    for i in range(3):
        for j in range(3):
            state_string += puzzle_state[i][j]
    return state_string


def get_path_to_goal(node):
    path = []  # path from end to start
    while node is not None:
        path.append(node.state)
        node = node.parent
    return path[::-1]  # reversed to get correct sequence from start to end


def solve_puzzle_A_star(puzzle, metric_type):
    start_time = time.time()
    goal_state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]
    visited_nodes = []
    frontier = []  # heapq with items being tuples in the format (heuristic_cost, frontier_insertion_count, node)
    visited_states_set = set()
    frontier_states_set = set()
    search_depth = 0
    frontier_insertion_count = 1

    root = Node(puzzle, None, 0, metric_type)
    visited_nodes.append(root)
    visited_states_set.add(state_to_string(root.state))
    if root.state == goal_state:
        return get_path_to_goal(root)

    for child_state in root.children:
        child_as_puzzle = Puzzle()
        child_as_puzzle.set_state(child_state)
        child_node = Node(child_as_puzzle, root, root.cost_to_reach_node + 1, metric_type)
        heappush(frontier, (child_node.heuristic_cost + child_node.cost_to_reach_node, frontier_insertion_count, child_node))
        frontier_states_set.add(state_to_string(child_state))
        frontier_insertion_count += 1

    trial_no = 1
    while len(frontier) > 0:
        # expanding node with the least heuristic cost
        node_to_expand = heappop(frontier)[2]
        visited_nodes.append(node_to_expand)
        visited_states_set.add(state_to_string(node_to_expand.state))
        if search_depth < node_to_expand.cost_to_reach_node:
            search_depth = node_to_expand.cost_to_reach_node
        node_in_puzzle_form = Puzzle()
        node_in_puzzle_form.set_state(node_to_expand.state)
        for child_state in node_to_expand.children:
            child_as_puzzle = Puzzle()
            child_as_puzzle.set_state(child_state)
            child_node = Node(child_as_puzzle, node_to_expand, node_to_expand.cost_to_reach_node + 1, metric_type)

            exists_in_frontier_or_visited = False
            if state_to_string(child_state) in frontier_states_set or state_to_string(child_state) in visited_states_set:
                exists_in_frontier_or_visited = True

            if not exists_in_frontier_or_visited:
                heappush(frontier, (child_node.heuristic_cost + child_node.cost_to_reach_node, frontier_insertion_count, child_node))
                frontier_states_set.add(state_to_string(child_state))
                frontier_insertion_count += 1

        print(f"\nExplored Node no: {trial_no}")
        node_in_puzzle_form.print_puzzle()

        if node_to_expand.state == goal_state:
            end_time = time.time()
            print(f"Puzzle solved successfully with A* {metric_type}")
            print(f"Path cost = {node_to_expand.cost_to_reach_node}")
            print(f"Search depth = {search_depth}")
            print(f"Running time = {end_time - start_time}")
            print("///////////////////////////////////////////////////////////")
            # return get_visited_nodes_states(visited_nodes)
            return get_path_to_goal(node_to_expand)

        trial_no += 1
    print("Failed to solve puzzle with A*")
