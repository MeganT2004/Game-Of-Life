import random
import os
from os import system
import time
import sys
import argparse
import pygame

parser = argparse.ArgumentParser()
parser.add_argument("-z", "--size", help="choose the size of the grid", type=int, default=25)
parser.add_argument("-p", "--speed", help="choose the speed of the grid", type=float, default=30)
parser.add_argument("-f", "--file", help="choose your own pre-set file to use", default=os.environ.get('FILE', None))
parser.add_argument("-b", "--birth", help="define the birth rules (between 1 and 9)", type=int, default=3)
parser.add_argument("-s", "--survival", help="define the survival rules of the game (between 1 and 9)", type=int, default=2)
parser.add_argument("-pre", "--presetRules", help="Choose preset survival rules for the game. Use '--rules' to see preset rules.", type=str, default=os.environ.get('PRESETRULES', None))
parser.add_argument("-r", "--rules", help="Displays preset rule types. Type 'True' to see.", type=bool, default=False)
parser.add_argument("-UI", "--UserInterface", help="Choose whether you wan to use the pyGame UI or the Command Line. (False if command line is wanted)", type=bool, default=True)

args = parser.parse_args()
size = (args.size)
speed = (args.speed)
preRules = (args.presetRules)

rules = (args.rules)
if rules == True:
    print("\nRule (Code):\t\t\tDescription:\n\nSeeds (SeedRule.py):\t\tEvery alive cell dies but 2 neighbours are born.\nLife Without Death (LWD.py):\t3 neighbours are needed to be born, but cells never die.\nDay and Night (DayAndNight.py):\tVery interesting rules creating strange patterns.\n")
    sys.exit()

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

class PyGameOutputter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()

    def print_grid(self, grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        cellWidth = 400 / len(grid)
        cellHeight = 400 / len(grid)

        for rowIndex, row in enumerate(grid):
            for cellIndex, cell in enumerate(row):
                rect = pygame.Rect(cellWidth*cellIndex,rowIndex*cellHeight,cellWidth,cellHeight)
                if cell == 0:
                    pygame.draw.rect(self.screen, (255,255,255), rect)
                elif cell == 1:
                    pygame.draw.rect(self.screen, (0,0,0), rect)
                elif cell == 2:
                    pygame.draw.rect(self.screen, (169,169,169), rect)
                elif cell == 3:
                    pygame.draw.rect(self.screen, (220,220,220), rect)
        pygame.display.update()
        self.clock.tick(speed)

class CommandLineOutputter:
    def print_grid(self, grid):
        system('cls')
        for row in grid:
            for cell in row:
                if cell == 0:
                    print('  ', end='')
                elif cell == 1:
                    print('██', end='')
                elif cell == 2:
                    print('▒▒', end='')
                elif cell == 3:
                    print('░░', end='')
            print()
        time.sleep(1.0/speed)

class Game:
    def __init__(self, grid):
        self.grid = grid
        UI = (args.UserInterface)
        if UI == False:
            self.ouputter = CommandLineOutputter()
        else:
            self.ouputter = PyGameOutputter()

    def Neighbour_Counts(self, cellX, cellY):
        aliveNeighboursCount = 0
        for x in [cellX - 1, cellX, cellX + 1]:
            for y in [cellY - 1, cellY, cellY + 1]:
                x = x % len(self.grid)
                y = y % len(self.grid)
                if x == cellX and y == cellY:
                    pass
                elif self.grid[x][y] == 1:
                    aliveNeighboursCount += 1
        return aliveNeighboursCount

    def New_State(self):
        B = (args.birth)
        S = (args.survival)
        newGrid = [[0 for _ in row] for row in self.grid]
        for x, row in enumerate(self.grid):
                for y, cellState in enumerate(row):
                    aliveNeighboursCount = self.Neighbour_Counts(x, y)
                    newCellState = cellState
                    if S == 0:
                        pass
                    elif cellState == 1:
                        if aliveNeighboursCount < S:
                            newCellState = 2 
                        elif aliveNeighboursCount > B:
                            newCellState = 2        
                        elif aliveNeighboursCount == S or aliveNeighboursCount == B:
                            newCellState = 1
                    elif cellState == 0:
                        if aliveNeighboursCount == B:
                            newCellState = 1
                    elif cellState == 2:
                        if aliveNeighboursCount == B:
                            newCellState = 1
                        else:
                            newCellState = 3
                    elif cellState == 3:
                        if aliveNeighboursCount == B:
                            newCellState = 1
                        else:
                            newCellState = 0  
                    newGrid[x][y] = newCellState
        return newGrid

    def preset_rules(self):
        if not args.presetRules:
            self.New_State()
        
    def isGameOver(self):
        anyAlive = False
        for row in self.grid:
            for cellState in row:
                if cellState == 1:
                    anyAlive = True
        return anyAlive

    def restartGame(self):
        restart=input("Do you want to start again? (Y/N) ")
        if restart.upper() == "Y":
            grid = []
            for x in range(size):
                row = []
                for y in range(size):
                    row.append(random.randint(0, 1))
                grid.append(row)
            self.ouputter.print_grid(self.grid)
            self.run()
        elif restart.upper() == "N":
            sys.exit()
        else:
            restart=input("Do you want to start again? (Y/N) ")

    def run(self):
        generation = 0
        while self.isGameOver():
            self.ouputter.print_grid(self.grid)
            newGrid = self.New_State()
            if (newGrid == self.grid):
                print("The population has stagnated. You survived,", generation, "generations.")
                self.restartGame()
            self.grid = newGrid
            generation = generation + 1
        else:
            print("The population has died off. You survived,", generation, "generations.")
            self.restartGame()

    def run_file(self, preRules):
        generation = 0
        module = __import__(preRules.replace(".py", ""))
        while self.isGameOver():
            self.ouputter.print_grid(self.grid)
            newGrid = module.Rule(self.Neighbour_Counts, self.grid)
            if (newGrid == self.grid):
                print("The population has stagnated. You survived,", generation, "generations.")
                self.restartGame()
            self.grid = newGrid
            generation = generation + 1
        else:
            print("The population has died off. You survived,", generation, "generations.")
            self.restartGame()

if (args.file != None) and (args.presetRules != None):
    game = Game(read_grid(file_path))
    game.run_file(preRules)
elif (args.file != None):
    game = Game(read_grid(file_path))
    game.run()
elif (args.presetRules != None):
    game = Game(random_grid())
    game.run_file(preRules)
else:
    game = Game(random_grid())
    game.run()


    



