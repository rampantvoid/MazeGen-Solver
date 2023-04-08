'''Main file'''

from solver import *
from maze_gen import *


def display(maze, size):
    print('\n...................................................................................\n')
    for i in range(size):
        for j in range(size):
            print(maze[i][j], end='')
        print()


print("\nWelcome! Get to know how your real world navigation problems are solved here with help of mazes\n")

while True:

    opt = input(
        "To start enter size(<= 50) of the maze(2D square matrix) to be generated(Enter 'Q' or 'q' to quit) : ")

    if (opt == 'q' or opt == 'Q') or int(opt) > 50:
        break

    size = int(opt)
    print('Generating a Maze of size {n}. . .'.format(n=size))
    maze = Maze(size)
    regen = input("\n\nRegenerate Maze?('Y'or'N') : ")

    while (regen.lower() != 'n'):
        print('Generating a Maze of size {n}. . .'.format(n=size))
        maze = Maze(size)
        regen = input("\n\nRegenerate Maze?('Y'or'N') : ")

    print('\n\nTake your time and analyze the maze think of it as a very low resolution pixeliated google map \nand you want to travel from Top Left corner to Bottom Right corner.\n')
    print('You can even try and solve the maze if you believe your are faster than a computer ;)\n')

    response = input(
        "Give Up? Enter 'solve' or 'SOLVE' to generate a solution for the maze : \n")

    count = 0
    while (response.lower() != 'solve'):

        count += 1
        response = input(print('Please Enter a Valid response! :\n'))

        if count > 3:
            print('Too many tries. Reseting Program')
            break

    print("Genrerating Solution in 3...2..\n")
    solve(maze, size)
    print("Sucessfuly Generated Solution!")
    display(maze, size)
    print("\nHave a look at the maze the solution path is marked with '*' symbol")
    # print("Just like that within a second we generated our path to the destination.\nNow you can imagine how our navigation system navigates us through roads!\n\n")

print("Thank you for using this program. Have a nice day :)")
