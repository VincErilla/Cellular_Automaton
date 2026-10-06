import matplotlib
import numpy as np
from display_grid import DisplayGrid


rows = 8
cols = 8

# Create an 8x8 grid filled with 0s (dead cells)
grid = [[0 for _ in range(rows)] for _ in range(cols)]

def countNeighbors(grid, r, c, edge_mode="dead"): # edge_mode is used to handle cells outside grid
    live_neighbors = 0

    # check surroundings of the cell
    for dr in [-1, 0, 1]: # values for row change (left, none, right)
        for dc in [-1, 0, 1]: # values for col change (up, none, down)
            if dr == 0 and dc == 0:
                continue

            nr, nc = r + dr, c + dc # neighbor cell row and column

            # two ways to handle cells outside grid
            if edge_mode == "dead":
                if 0 <= nr < rows and 0 <= nc < cols: # checks neighbors in valid bounds only
                    live_neighbors += grid[nr][nc] # counts amount of neighbors that are alive
            
            # if current cell is on perimeter, it will check the neighbors on the oposite side, not outside the grid.
            elif edge_mode == "wrap":
                live_neighbors += grid[nr % rows][nc % cols] # 

    return live_neighbors


def nextGeneration():

    pass


def printGrid(grid):
    print("-" * (len(grid[0]) * 2 + 1)) # prints a top border

    for row in grid:
        line = " ".join("#" if cell == 1 else "." for cell in row) # Dead = 0(.), Alive = 1(#)
        print(f"| {line} |")

    print("-" * (len(grid[0])* 2 + 1))


def main():
    printGrid(grid)

if __name__ == "__main__":
    main()


