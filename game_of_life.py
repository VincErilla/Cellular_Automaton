import matplotlib
import numpy as np
import utils
from copy import deepcopy

class CellGrid:
    def __init__(self, rows, cols, edge_mode="dead"):
        self.edge_mode = edge_mode
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)] #makes 0s grid
        self.rules = utils.loadRules()

    def countNeighbors(self, grid, row, col): # edge_mode is used to handle cells outside grid
        live_neighbors = 0
        # check surroundings of the cell
        for d_row in [-1, 0, 1]: # values for row change (left, none, right)
            for d_col in [-1, 0, 1]: # values for col change (up, none, down)
                if d_row == 0 and d_col == 0:
                    continue

                neighbor_row, neighbor_col = row + d_row, col + d_col # neighbor cell row and column

                # two ways to handle cells outside grid
                if self.edge_mode == "dead":
                    if 0 <= neighbor_row < self.rows and 0 <= neighbor_col < self.cols: # checks neighbors in valid bounds only
                        live_neighbors += grid[neighbor_row][neighbor_col] # counts amount of neighbors that are alive
                # if current cell is on perimeter, it will check the neighbors on the oposite side, not outside the grid.
                elif self.edge_mode == "wrap":
                    live_neighbors += grid[neighbor_row % self.rows][neighbor_col % self.cols] # 

        return live_neighbors


    def nextGeneration(self):
        oldGrid = deepcopy(self.grid)
        for row in range(self.rows):
            for col in range(self.cols):
                neighbor_count = self.countNeighbors(oldGrid, row, col)
                if neighbor_count in self.rules["birth"]:
                    self.grid[row][col] = 1
                elif oldGrid[row][col] == 1 and neighbor_count in self.rules["survive"]:
                    self.grid[row][col] = 1
                else:
                    self.grid[row][col] = 0

        del oldGrid

    def printGrid(self):
        print("-" * (len(self.grid[0]) * 2 + 1)) # prints a top border

        for row in self.grid:
            line = " ".join("#" if cell == 1 else "." for cell in row) # Dead = 0(.), Alive = 1(#)
            print(f"| {line} |")

        print("-" * (len(self.grid[0])* 2 + 1))


def main():
    grid = CellGrid(8, 9)
    grid.printGrid()
    grid.nextGeneration()
    grid.printGrid()

if __name__ == "__main__":
    main()


