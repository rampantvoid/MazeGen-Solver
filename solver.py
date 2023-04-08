'''Uses recursion and backtracking to solve a maze and diplay the path'''

# importing our maze generator as a module
from maze_gen import *


def isSafe(x, y, visited, maze, size):
    '''Return boolean value after checking if current cell is a valid path

    :param x = X coordinate for current cell
    :param y : Y coordinate for current cell
    :visited : 2D Boolean Square Matrix
    :maze : 2D Square Matrix maze
    :size : size of matrix

    :return : True if cell is a valid path is possible
    :return : False if cell is not a valid path

    '''

    if x > 0 and x < size-1 and y > 0 and y < size-1 and visited[x][y] != 1 and maze[x][y] == ' ':

        return True

    return False


def find_solution(curr_x, curr_y, maze, size, visited, sol):
    '''Traces the solution path on the Maze

    :param curr_x = X coordinate of current cell
    :param curr_y : Y coordinate of current cell
    :param maze : 2D square Matrix Maze
    :visited : 2D Boolean Square Matrix
    :param size : size of matrix
    :param sol : hold the coordinates of cells([x,y]) which forms the solution

    :return : None

    '''

    # base case and mark the solution

    if curr_x == size-2 and curr_y == size-2:
        for i in sol:
            maze[i[0]][i[1]] = '*'
        return

    # maintain for cells which have been visited
    visited[curr_x][curr_y] = 1

    # check left
    if isSafe(curr_x+1, curr_y, visited, maze, size):

        # if cell is valid append it to solutin
        sol.append([curr_x+1, curr_y])

        # RECURSIVE CALL
        find_solution(curr_x+1, curr_y, maze, size, visited, sol)

        # BACKTRACK
        sol.pop()

    # check right
    if isSafe(curr_x-1, curr_y, visited, maze, size):
        sol.append([curr_x-1, curr_y])
        find_solution(curr_x-1, curr_y,  maze, size, visited, sol)
        sol.pop()

    # check up
    if isSafe(curr_x, curr_y+1, visited, maze, size):
        sol.append([curr_x, curr_y+1])
        find_solution(curr_x, curr_y+1,  maze, size, visited, sol)
        sol.pop()

    # check down
    if isSafe(curr_x, curr_y-1, visited, maze, size):
        sol.append([curr_x, curr_y-1])
        find_solution(curr_x, curr_y-1,  maze, size, visited, sol)
        sol.pop()


def solve(maze, size):
    '''Generates a boolean map for maintaing visited cells and calls function to find paths.

    :param maze : Takes our 2D Matrix
    :param size : size of out matrix

    :return : None

    '''
    # put starting cell as top left cell
    start_x, start_y = 1, 1
    sol = []
    visited = []

    # initialize visited matrix with 0 in correspondance to our maze
    for i in range(size):
        a = []
        for j in range(size):
            a.append(0)
        visited.append(a)

    # function calling to find solution
    find_solution(start_x, start_y, maze, size, visited, sol)
