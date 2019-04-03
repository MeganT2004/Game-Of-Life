import random
import os
from os import system
import time
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-z", "--size", help="choose the size of the grid", type=int, default=5)
parser.add_argument("-p", "--speed", help="choose the speed of the grid", type=float, default=0.2)
parser.add_argument("-f", "--file", help="choose your own pre-set file to use", default=os.environ.get('FILE', None))

args = parser.parse_args()
size = (args.size)
speed = (args.speed)

def random_grid():
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.randint(0, 1))
        grid.append(row)
    return grid

file_path = (args.file)
if not args.file:
    random_grid()

def read_grid(file_path):
    grid = []
    with open(file_path, 'r') as f:
        data = f.readlines()
        for line in data:
            row = []
            for character in line:
                if character == '0':
                    row.append(0)
                elif character == '1':
                    row.append(1)
            grid.append(row)
    return grid


def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                print('  ', end='')
            else:
                print('██', end='')
        print()

def Neighbour_Counts(grid, cellX, cellY):
    aliveNeighboursCount = 0
    for x in [cellX - 1, cellX, cellX + 1]:
        for y in [cellY - 1, cellY, cellY + 1]:
            x = x % len(grid)
            y = y % len(grid)
            if x == cellX and y == cellY:
                pass
            elif grid[x][y] == 1:
                aliveNeighboursCount += 1
    return aliveNeighboursCount

def New_State(grid):
    newGrid = [[0 for _ in row] for row in grid]
    for x, row in enumerate(grid):
            for y, cellState in enumerate(row):
                aliveNeighboursCount = Neighbour_Counts(grid, x, y)
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

def isGameOver(grid):
    anyAlive = False
    for row in grid:
        for cellState in row:
            if cellState == 1:
                anyAlive = True
    return anyAlive

def restartGame():
    restart=input("Do you want to start again? (Y/N) ")
    if restart.upper() == "Y":
        grid = []
        for x in range(size):
            row = []
            for y in range(size):
                row.append(random.randint(0, 1))
            grid.append(row)
        print_grid(grid)
        run(grid)
    elif restart.upper() == "N":
        sys.exit()
    else:
        restart=input("Do you want to start again? (Y/N) ")

def run(grid):
    generation = 0
    while isGameOver(grid):
        system('cls')
        print_grid(grid)
        print("Generaion: ", generation)
        newGrid = New_State(grid)
        if (newGrid == grid):
            print("The population has stagnated. You survived,", generation, "generations.")
            restartGame()
        grid = newGrid
        generation = generation + 1
        time.sleep(speed)
    else:
        print("The population has died off. You survived,", generation, "generations.")
        restartGame()

if (args.file != None):
    run(read_grid(file_path))
else:
    run(random_grid())


    



