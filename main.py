'''Main file'''

from solver import *
from maze_gen import *


def display(maze, size):
    print('\n...................................................................................\n')
    for i in range(size):
        for j in range(size):
            print(maze[i][j], end='')
        print()
