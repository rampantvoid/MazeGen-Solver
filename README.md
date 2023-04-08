
# Maze Generator & Solver

This is a Python program that generates a maze of a given size, and then allows the user to generate a solution for it. The program uses a randomized Depth-First-Search algorithm to generate the maze. And using recursion and backtracking generates a solution.




# Usage
```bash
$ git clone https://github.com/rampantvoid/MazeGen-Solver
$ cd MazeGen-Solver
```
After downloading the repository run the ```main.py``` python file
```bash
$ python3 main.py
```



# Documentation
## ```main.py```
The main file ```main.py``` contains the entry point of the program. It prompts the user to enter the size of a 2D square matrix, which will be used to generate a maze of the specified size. The program then allows the user to regenerate the maze as many times as they want.

Once the maze is generated, the user is prompted to solve the maze by entering "solve".

When the user enters "solve", the program generates a solution to the maze using the solve function from ```solver.py```.

The solution is then displayed to the user, with the path marked by a '*' symbol.

The ```display()``` function is used to print the maze and its solution in a readable format. It takes the maze and its size as input parameters and prints them to the console.

## ```maze_gen.py```
This code generates a maze using the Randomized Depth First Search algorithm (also known as the Recursive Backtracker algorithm). The maze is generated as a 2D square matrix of size n x n. The algorithm starts at a random cell and selects a path to a new cell until it reaches the end cell.

### Functions

#### ```Valid_neighbours(curr_x, curr_y, maze, n, neighbours)```

        This function returns all the valid neighbours of the selected cell. 


#### ```surrCells(rand_cell, maze)```

        This function returns the count of already traced path cells around these 
        selected cell.
#### ```generate_Paths(curr_x, curr_y, end_x, end_y, maze, size)```
        This function generates paths with Recursive Backtracking

        Returns True when the maze is generated successfully.
        False when it cannot go further and backtracks to the last cell with possible 
        neighbours.
#### ```Maze(size)```
        This function generates a maze using the Randomized Depth First Search algorithm 
        by calling all the other functions and displays it.
    
## ```solver.py```
This program uses recursion and backtracking to solve a maze and display the path. It takes a maze of size n x n as input, generates a boolean map for maintaining visited cells, and then calls the find_solution() function to find the paths.

### Functions

#### ```isSafe(x, y, visited, maze, size)```

        This function takes in the current cell's x and y coordinates, a boolean matrix 
        representing visited cells, the maze, and its size as parameters. It checks if the 
        current cell is a valid path. 


#### ```find_solution(curr_x, curr_y, maze, size, visited, sol)```

        This function generates a possible path to destination and appends cells forming 
        that path to a list to holding the coordinates of cells. And it traces the 
        solution path on the maze using recursion and backtracking.

        Note: This function modifies the maze in place by marking the cells that form the 
        solution path with "*".
    
#### ```solve(maze,size)```
        The solve() function is the main function that calls the other two functions to 
        solve the maze.


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Credits

This program was created by Priyanshu Butola.