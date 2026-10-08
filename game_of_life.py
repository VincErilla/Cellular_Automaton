import numpy as np
import utils
from display_grid import DisplayGrid
from copy import deepcopy

class CellGrid:
    def __init__(self):
        self.rules = utils.loadRules()
        self.edge_mode = "wrap" if self.rules["edge_wrap"] == True else "dead"
        self.rows = self.rules["width"]
        self.cols = self.rules["height"]
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)] #makes 0s grid


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
        oldGrid = deepcopy(self.grid) # makes a copy of the grid
        for row in range(self.rows):
            for col in range(self.cols):
                neighbor_count = self.countNeighbors(oldGrid, row, col) # references the copy to update the original
                if neighbor_count in self.rules["birth"]:
                    self.grid[row][col] = 1
                elif oldGrid[row][col] == 1 and neighbor_count in self.rules["survive"]:
                    self.grid[row][col] = 1
                else:
                    self.grid[row][col] = 0
                    
        del oldGrid # yippee we love not having memory leaks

    def printGrid(self):
        print("-" * (len(self.grid[0]) * 2 + 1)) # prints a top border

        for row in self.grid:
            line = " ".join("#" if cell == 1 else "." for cell in row) # Dead = 0(.), Alive = 1(#)
            print(f"| {line} |")

        print("-" * (len(self.grid[0])* 2 + 1))

    def save(self):
        utils.saveState(self.grid)

    def load(self):
        newGrid = utils.loadState()
        if len(newGrid) == len(self.grid) and len(newGrid[0]) == len(self.grid[0]):
            self.grid = newGrid
        else:
            print(f"Error loading grid: Dimension Mismatch (Current grid is {len(self.grid)}x{len(self.grid[0])}, Saved grid is {len(newGrid)}x{len(newGrid[0])})")


def main():
    grid = CellGrid()
    display = DisplayGrid(grid)
    display.control_main_loop(delay=0.1)

if __name__ == "__main__":
    main()


