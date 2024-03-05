from puzzle import Puzzle

import copy
import random

count = 0
SOLUTION=[[
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]]


def print_mat(matrix):
    matrix=matrix.state
    for i in range(0,3):
            print(str(matrix[i][0])+"|"+str(matrix[i][1])+"|"+str(matrix[i][2]))
def is_matrix_in_list(matrix, list_of_matrices):

  # Check if any matrix in the list is equal to the given matrix
  for other_matrix in list_of_matrices:
    if all(all(a == b for a, b in zip(row1, row2)) for row1, row2 in zip(matrix, other_matrix)):
      return True

  return False
def is_matrix_Visited(matrix, list_of_matrices):

  # Check if any matrix in the list is equal to the given matrix
  for other_matrix in list_of_matrices:
    # print_mat(other_matrix)
    if all(all(a == b for a,  b in zip(row1, row2)) for row1, row2 in zip(matrix, other_matrix.state)):
      return True

  return False


def get_children(state):
    row =0
    column=0
    children=[]
    for i in range(0,3):
        for j in range(0,3):
            if state[i][j]=="0":
                row=i
                column=j
                break
        if state[i][j] == "0":
            row = i
            column = j
            break
    if (row==0 or row==2) and (column==0 or column==2):
        temp1=copy.deepcopy(state)
        temp2=copy.deepcopy(state)
        temp1[row][column],temp1[abs(row-1)][column]=temp1[abs(row-1)][column],temp1[row][column]

        temp2[row][column], temp2[row][abs(column-1)] = temp2[row][abs(column-1)], temp2[row][column]
        list = []
        list.append(temp1)
        list.append(temp2)
        for i in range(0, 2):
            index = random.randrange(len(list))
            children.append(list.pop(index))

    elif (row==1) and (column==1):
        temp1=copy.deepcopy(state)
        temp1[row][column],temp1[(row-1)][column]=temp1[(row-1)][column],temp1[row][column]
        temp2 = copy.deepcopy(state)
        temp2[row][column], temp2[row][(column-1)] = temp2[row][(column-1)], temp2[row][column]
        list = []
        list.append(temp1)
        list.append(temp2)

        temp3 = copy.deepcopy(state)
        temp3[row][column], temp3[(row + 1)][column] = temp3[(row + 1)][column], temp3[row][column]
        temp4 = copy.deepcopy(state)
        temp4[row][column], temp4[row][(column + 1)] = temp4[row][(column + 1)], temp4[row][column]
        list.append(temp3)
        list.append(temp4)
        for i in range(0,4):
            index = random.randrange(len(list))
            children.append(list.pop(index))
    else:
        temp1 = copy.deepcopy(state)
        temp1[row][column], temp1[abs(row - 1)][column] = temp1[abs(row - 1)][column], temp1[row][column]
        temp2 = copy.deepcopy(state)
        temp2[row][column], temp2[row][abs(column - 1)] = temp2[row][abs(column - 1)], temp2[row][column]
        list=[]
        list.append(temp1)
        list.append(temp2)
        index = random.randrange(len(list))


        if column==1:
            temp3 = copy.deepcopy(state)
            temp3[row][column], temp3[row][(column + 1)] = temp3[row][(column + 1)], temp3[row][column]

        elif row==1:
            temp3 = copy.deepcopy(state)
            temp3[row][column], temp3[row+1][column] = temp3[row+1][column], temp3[row][column]

        list.append(temp3)
        list.append(temp1)
        list.append(temp2)
        for i in range(0, 3):
            index = random.randrange(len(list))
            children.append(list.pop(index))
    return children



class DFSNode:
    def __init__(self,puzzle):
        self.state=puzzle.state
        self.children=get_children(self.state)
        self.depth=1
        self.parent=None




import time
def visit(p,visited_nodes,frontier):
    # time.sleep(5)
    # if len(visited_nodes)%1000==0:
    #     print(len(visited_nodes))


    # print_mat(p)
    visited_nodes.append(p)
    if is_matrix_in_list(p.state, SOLUTION):
        # print("done")
        return True
    else:

        node=p
        for child in node.children:
            pu = Puzzle()
            pu.set_state(child)
            if is_matrix_Visited(child,frontier) or is_matrix_Visited(child,visited_nodes) :
                continue
            y=DFSNode(pu)
            y.depth=p.depth+1
            y.parent=node
            frontier.append(y)


def solve_puzzleBFS(puzzle):
    goal_state = [
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]

    visited_nodes = []
    frontier = []
    root = DFSNode(puzzle)
    root.depth=1
    visited_nodes.append(root)
    for child in root.children:
        pu=Puzzle()
        # print("#########")
        pu.set_state(child)
        ch=DFSNode(pu)
        ch.parent=root
        frontier.append(ch)
        # pu.print_puzzle()
    solveable=False
    path=[]
    while len(frontier)>0:
        if visit(frontier.pop(0), visited_nodes, frontier):
            solveable=True
            break


    if solveable==True:
        # print("solved succesfully ")
        # print(visited_nodes[-1].depth)
        current=visited_nodes[-1]
        while current.parent:
            # print_mat(current)
            path.append(current.state)
            # print("###########################")

            current=current.parent
        # print(len(path))

        return path
    else:
        return False

        print_mat(visited_nodes[0])




p = Puzzle()
p.shuffle_puzzle()

w=solve_puzzleBFS(p)
print(len(w))
print(((w)))


