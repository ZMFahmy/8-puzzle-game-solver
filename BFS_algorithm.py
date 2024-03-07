from puzzle import Puzzle

import copy
import random

count = 0
SOLUTION=[[
            ["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"],
    ]]

def reshape(matrix):
    l=[]
    for i in range(0,3):
        for j in range(0, 3):
            l.append(matrix[i][j])
    # print(l)
    w= ''.join(l)
    return w

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
    st=other_matrix.state
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j]!=st[i][j]:
                return False
    return True

  return False


def get_children(state):
    row = 0
    column = 0
    children = []
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == "0":
                row = i
                column = j
                break
        if state[row][column] == "0":
            row = i
            column = j
            break
    if (row == 0 or row == 2) and (column == 0 or column == 2):
        temp1 = copy.deepcopy(state)
        temp2 = copy.deepcopy(state)
        temp1[row][column], temp1[abs(row - 1)][column] = temp1[abs(row - 1)][column], temp1[row][column]

        temp2[row][column], temp2[row][abs(column - 1)] = temp2[row][abs(column - 1)], temp2[row][column]
        list = []
        list.append(temp1)
        list.append(temp2)
        for i in range(0, 2):
            index = random.randrange(len(list))
            children.append(list.pop(index))

    elif (row == 1) and (column == 1):
        temp1 = copy.deepcopy(state)
        temp1[row][column], temp1[(row - 1)][column] = temp1[(row - 1)][column], temp1[row][column]
        temp2 = copy.deepcopy(state)
        temp2[row][column], temp2[row][(column - 1)] = temp2[row][(column - 1)], temp2[row][column]
        list = []
        list.append(temp1)
        list.append(temp2)

        temp3 = copy.deepcopy(state)
        temp3[row][column], temp3[(row + 1)][column] = temp3[(row + 1)][column], temp3[row][column]
        temp4 = copy.deepcopy(state)
        temp4[row][column], temp4[row][(column + 1)] = temp4[row][(column + 1)], temp4[row][column]
        list.append(temp3)
        list.append(temp4)
        for i in range(0, 4):
            index = random.randrange(len(list))
            children.append(list.pop(index))
    else:
        # temp1 = copy.deepcopy(state)
        # temp1[row][column], temp1[abs(row - 1)][column] = temp1[abs(row - 1)][column], temp1[row][column]
        # temp2 = copy.deepcopy(state)
        # temp2[row][column], temp2[row][abs(column - 1)] = temp2[row][abs(column - 1)], temp2[row][column]
        # list = []
        # list.append(temp1)
        # list.append(temp2)
        # index = random.randrange(len(list))

        if column == 1:
            temp3 = copy.deepcopy(state)
            temp3[row][column], temp3[row][2] = temp3[row][2], temp3[row][column]
            temp1 = copy.deepcopy(state)
            temp1[row][column], temp1[1][1] = temp1[1][1], temp1[row][column]
            temp2 = copy.deepcopy(state)
            temp2[row][column], temp2[row][column - 1] = temp2[row][column - 1], temp2[row][column]
            list = []
            list.append(temp1)
            list.append(temp2)
            # index = random.randrange(len(list))

        elif row == 1:
            temp3 = copy.deepcopy(state)
            temp3[row][column], temp3[2][column] = temp3[2][column], temp3[row][column]
            temp1 = copy.deepcopy(state)
            temp1 = copy.deepcopy(state)
            temp1[row][column], temp1[1][1] = temp1[1][1], temp1[row][column]
            temp2 = copy.deepcopy(state)
            temp2[row][column], temp2[row - 1][abs(column)] = temp2[row - 1][abs(column)], temp2[row][column]
        list = []

        # index = random.randrange(len(list))

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
def visit(p,visited_nodes,frontier,VisitedSet):
    # time.sleep(5)
    # if len(visited_nodes)%1000==0:
    #     print(len(visited_nodes))

    print("exploring node ",len(visited_nodes))
    print_mat(p)
    visited_nodes.append(p)
    VisitedSet.add(reshape(p.state))
    if is_matrix_in_list(p.state, SOLUTION):
        # print("done")
        return True
    else:

        node=p
        for child in node.children:
            pu = Puzzle()
            pu.set_state(child)
            if is_matrix_Visited(child,frontier) or reshape(child) in VisitedSet :
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
    t1=time.time()
    visited_nodes = []
    VisitedSet = set()

    frontier = []
    root = DFSNode(puzzle)
    root.depth=1
    visited_nodes.append(root)
    VisitedSet.add(reshape(root.state))
    path=[]
    if is_matrix_in_list(root.state,SOLUTION):
        # path.append(root.state)
        return path
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
    # path.append(root.state)
    while len(frontier)>0:
        if visit(frontier.pop(0), visited_nodes, frontier,VisitedSet):
            solveable=True
            break


    if solveable==True:
        # print("solved succesfully ")
        # print(visited_nodes[-1].depth)
        current=visited_nodes[-1]
        t2=time.time()
        dddepth=current.depth
        print("time taken for BFS = ",t2-t1)
        print("the height is ", dddepth)
        # for i in range(0,len(visited_nodes)):
        #     dep=0
        #     l=[]
        #
        #     nod=visited_nodes.pop(0)
        #     if nod.depth>dep:
        #         print(l)
        #         dep+=1
        #     l.append(nod)

        while current.parent:
            # print_mat(current)
            path.insert(0,current.state)
            # print("###########################")

            current=current.parent
        # print(len(path))

        return path
    else:
        return False

        print_mat(visited_nodes[0])


#
#
import time

# p=Puzzle()
# print(p.state)
# p.set_state([["1",'2','0'],['3','4','5'],['6','7','8']])
# print(p.state)
# t1=time.time()
# x=solve_puzzleBFS(p)
# print(len(x),x)
#
# t2=time.time()
# print(t2-t1)


