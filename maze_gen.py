import random


def neighbours(curr_x, curr_y, end_x, end_y, maze, n, walls):

    if curr_x > 1 and maze[curr_x-1][curr_y] != ' ':  # left
        walls.append([curr_x-1, curr_y])

    if curr_x < n-2 and maze[curr_x+1][curr_y] != ' ':  # right
        walls.append([curr_x+1, curr_y])

    if curr_y > 1 and maze[curr_x][curr_y-1] != ' ':  # down
        walls.append([curr_x, curr_y-1])

    if curr_y < n-2 and maze[curr_x][curr_y+1] != ' ':  # up
        walls.append([curr_x, curr_y+1])


def surrCells(rand_cell, maze):

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


def generator(curr_x, curr_y, end_x, end_y, maze, n):

    maze[curr_x][curr_y] = ' '
    # base case
    if (curr_x == end_x and curr_y == end_y):
        print('done')
        return True

    neighbour = []
    neighbours(curr_x, curr_y, end_x, end_y, maze, n, neighbour)

    while (neighbour):
        next_x, next_y = neighbour[random.randint(0, len(neighbour)-1)]
        neighbour.remove([next_x, next_y])

        if surrCells([next_x, next_y], maze) < 2:
            if generator(next_x, next_y, end_x, end_y, maze, n):
                return True
    return False


maze = []
size = 50

for i in range(size):
    a = []
    for j in range(size):
        a.append('#')

    maze.append(a)

start_x, start_y = 1, 1
end_x, end_y = size-2, size-2

curr_x, curr_y = start_x, start_y


maze[curr_x][curr_y] = ' '
generator(curr_x, curr_y, end_x, end_y, maze, size)

maze[curr_x][curr_y] = '*'
maze[end_x][end_y] = '*'

for i in range(size):
    for j in range(size):
        print(maze[i][j], end=" ")
    print()
