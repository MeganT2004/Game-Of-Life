import random
from os import system
import time
size = 50

grid = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(random.randint(0, 1))
    grid.append(row)
    
def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                print('  ', end='')
            else:
                print('██', end='')
        print()

def Neighbour_Counts(x, y):
    aliveNeighboursCount = 0
    if grid[x - 1][y -1] == 1:
        aliveNeighboursCount += 1
    if grid[x -1][y] == 1:
        aliveNeighboursCount += 1
    if y < size - 1 and grid[x -1][y + 1] == 1:
        aliveNeighboursCount += 1

    if y < size - 1 and grid[x][y + 1] == 1:
        aliveNeighboursCount += 1
    if grid [x][y - 1] == 1:
        aliveNeighboursCount += 1

    if x < size - 1 and grid [x + 1][y] == 1:
        aliveNeighboursCount += 1
    if x < size -1 and grid[x + 1][y - 1] == 1:
        aliveNeighboursCount += 1
    if x < size - 1 and y < size - 1 and grid[x + 1][y + 1] == 1:
        aliveNeighboursCount += 1
    return aliveNeighboursCount

def New_State():
    newGrid = [[0 for x in range(size)] for y in range(size)]
    for x in range(size):
            for y in range(size):
                aliveNeighboursCount = Neighbour_Counts(x, y)
                cellState = grid[x][y]
                newCellState = cellState
                if aliveNeighboursCount < 2:
                    newCellState = 0
                if aliveNeighboursCount > 3:
                    newCellState = 0
                if aliveNeighboursCount == 3:
                    newCellState = 1
                if cellState == 0: 
                    if aliveNeighboursCount == 2 or aliveNeighboursCount == 3:
                        newCellState = 1
                newGrid[x][y] = newCellState
    return newGrid

while True:
    system('cls')
    print_grid(grid)
    grid = New_State()
    time.sleep(0.2)