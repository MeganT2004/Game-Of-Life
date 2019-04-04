def Rule(Neighbour_Counts, grid):
    newGrid = [[0 for _ in row] for row in grid]
    for x, row in enumerate(grid):
            for y, cellState in enumerate(row):
                aliveNeighboursCount = Neighbour_Counts(x, y)
                newCellState = cellState
                if cellState == 1:
                        newCellState = 2
                elif cellState == 0:
                    if aliveNeighboursCount == 3:
                        newCellState = 1
                elif cellState == 2:
                    if aliveNeighboursCount == 3:
                        newCellState = 1
                    else:
                        newCellState = 3
                elif cellState == 3:
                    if aliveNeighboursCount == 3:
                        newCellState = 1
                    else:
                        newCellState = 0
                newGrid[x][y] = newCellState
    return newGrid