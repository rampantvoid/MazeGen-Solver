'''Uses Randamized Depth First Search(DFS)/Recursive Backtracker to Generate a Maze'''

import random


def Valid_neighbours(curr_x, curr_y, maze, n, neighbours):
    '''Returns all the valid neighbours of the selected cell.

    :param curr_x : x coordinate of cell
    :param curr_y : y coordinate of cell
    :param maze : 2D Square Matrix
    :param neighbours : Stores cell address([x,y]) of all valid neighbours in a list

    :return : list

    '''

    if curr_x > 1 and maze[curr_x-1][curr_y] != ' ':  # check left
        neighbours.append([curr_x-1, curr_y])

    if curr_x < n-2 and maze[curr_x+1][curr_y] != ' ':  # check right
        neighbours.append([curr_x+1, curr_y])

    if curr_y > 1 and maze[curr_x][curr_y-1] != ' ':  # check down
        neighbours.append([curr_x, curr_y-1])

    if curr_y < n-2 and maze[curr_x][curr_y+1] != ' ':  # check up
        neighbours.append([curr_x, curr_y+1])


def surrCells(rand_cell, maze):
    '''Returns count of already traced path cells around the selected cell.

    :param rand_cell : Takes coordinates of a cell([x,y]) selected at random from list of valid neighbours
    :param maze : 2D Square Matrix

    :return : count(int)

    '''
    count = 0
    if maze[rand_cell[0]-1][rand_cell[1]] == ' ':
        count += 1

    if maze[rand_cell[0]+1][rand_cell[1]] == ' ':
        count += 1

    if maze[rand_cell[0]][rand_cell[1]-1] == ' ':
        count += 1

    if maze[rand_cell[0]][rand_cell[1]+1] == ' ':
        count += 1

    return count


def generate_Paths(curr_x, curr_y, end_x, end_y, maze, size):
    '''Generates Paths with Recursive Backtracking

    :param curr_x : X coordinate of current cell
    :param curr_y : Y coordinate of current cell
    :param end_x : X coordinate of END cell
    :param end_y : Y coordinate of END cell
    :param maze : 2D Square Matrix
    :param size : size of the matrix/maze

    :return : Ture when maze is generated sucessfuly
    :returm : False when can't go further and backtracks to last cell with possible neighbours

    '''

    # set current cell as a path
    maze[curr_x][curr_y] = ' '

    # BASE CASE
    if (curr_x == end_x and curr_y == end_y):

        return True

    # get valid neighbours for current cell
    neighbour = []
    Valid_neighbours(curr_x, curr_y, maze, size, neighbour)

    # start selecting random cells and generating path
    while (neighbour):

        # pop a random neighbour from list of valid neighbours
        next_x, next_y = neighbour[random.randint(0, len(neighbour)-1)]
        neighbour.remove([next_x, next_y])

        # check for surrounding paths (important step: avoid making a blocky maze)
        if surrCells([next_x, next_y], maze) < 2:

            # RECURSIVE CALL(if False then check for another neighbour)
            if generate_Paths(next_x, next_y, end_x, end_y, maze, size):
                return True

    # return False if no more neighbours are left, backtrack to last neighbour with possible options
    return False


def Maze(size):
    '''Call this funtion in your code to generate a maze and display it'''

    maze = []

    start_x, start_y = 1, 1
    end_x, end_y = size-2, size-2

    for i in range(size):
        a = []
        for j in range(size):
            a.append('█')
        maze.append(a)

    generate_Paths(start_x, start_y, end_x, end_y, maze, size)

    maze[start_x][start_y] = '*'
    maze[end_x][end_y] = ' '

    for i in range(size):
        for j in range(size):
            print(maze[i][j], end='')
        print()

    return maze
