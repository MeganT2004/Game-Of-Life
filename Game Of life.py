import random
from os import system
import time
size = 50
# grid = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 1, 0],
#     [0, 0, 0, 0, 0]
# ]

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

def Neighbour_Counts(cellX, cellY):
    aliveNeighboursCount = 0
    for x in [cellX - 1, cellX, cellX + 1]:
        for y in [cellY - 1, cellY, cellY + 1]:
            #if x >= size:
            x = x % size
            #if y >= size:
            y = y % size
            if x == cellX and y == cellY:
                pass
            elif grid[x][y] == 1:
                aliveNeighboursCount += 1
            
    return aliveNeighboursCount

def New_State():
    newGrid = [[0 for x in range(size)] for y in range(size)]
    for x in range(size):
            for y in range(size):
                aliveNeighboursCount = Neighbour_Counts(x, y)
                cellState = grid[x][y]
                newCellState = cellState
                if cellState == 1:
                    if aliveNeighboursCount < 2:
                        newCellState = 0
                    if aliveNeighboursCount > 3:
                        newCellState = 0                    
                    if aliveNeighboursCount == 2 or aliveNeighboursCount == 3:
                        newCellState = 1
                        
                if cellState == 0:
                    if aliveNeighboursCount == 3:
                        newCellState = 1

                
                newGrid[x][y] = newCellState
    return newGrid

while True:
    system('cls')
    print_grid(grid)
    grid = New_State()
    time.sleep(0.5)