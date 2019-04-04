def Rule(Neighbour_Counts, grid):
    newGrid = [[0 for _ in row] for row in grid]
    for x, row in enumerate(grid):
            for y, cellState in enumerate(row):
                aliveNeighboursCount = Neighbour_Counts(x, y)
                newCellState = cellState
                if cellState == 1:
                    if aliveNeighboursCount == 3 or aliveNeighboursCount == 4 or aliveNeighboursCount == 6 or aliveNeighboursCount == 7 or aliveNeighboursCount == 8:
                        newCellState = 1
                    else:
                        newCellState = 2
                elif cellState == 0:
                    if aliveNeighboursCount == 3 or aliveNeighboursCount == 6 or aliveNeighboursCount == 7 or aliveNeighboursCount == 8:
                        newCellState = 1
                elif cellState == 2:
                    if aliveNeighboursCount == 3 or aliveNeighboursCount == 6 or aliveNeighboursCount == 7 or aliveNeighboursCount == 8:
                        newCellState = 1
                    else:
                        newCellState = 3
                elif cellState == 3:
                    if aliveNeighboursCount == 3 or aliveNeighboursCount == 6 or aliveNeighboursCount == 7 or aliveNeighboursCount == 8:
                        newCellState = 1
                    else:
                        newCellState = 0
                newGrid[x][y] = newCellState
    return newGrid