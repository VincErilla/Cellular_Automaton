import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class DisplayGrid:
    def __init__(self, grid):
        self.grid = grid
        self.fig, self.ax = plt.subplots()
        self.color_map = mpl.colors.ListedColormap(['black', 'white'])  # Black for dead cells, white for alive cells
        self.im = None
        plt.ion()  # Turn on interactive mode

    def display(self):
        self.im = self.ax.imshow(self.grid, cmap=self.color_map, 
                                 interpolation='nearest', vmin=0, vmax=1)
        plt.xticks([])  # Remove x-axis ticks
        plt.yticks([])  # Remove y-axis ticks
        plt.show(block=False)  # Non-blocking show to allow updates
        plt.pause(0.1)  # Pause to allow the plot to render

    def update_display(self, new_grid):
        self.grid = new_grid
        self.im.set_data(self.grid)
        plt.draw()
        plt.pause(0.5)

if __name__ == "__main__":
    # Example usage
    rows, cols = 8, 8
    grid = [[0 for _ in range(cols)] for _ in range(rows)]  
    display = DisplayGrid(grid)
    display.display()
    while plt.fignum_exists(display.fig.number):  # Keep updating as long as the figure window is open
        grid[0][0] = 1
        grid[1][1] = 1 
        grid[2][2] = 1
        grid[3][3] = 1
        grid[4][4] = 1
        grid[5][5] = 1
        grid[6][6] = 1
        grid[7][7] = 1
        grid[7][0] = 1
        grid[6][1] = 1
        grid[5][2] = 1
        grid[4][3] = 1
        grid[3][4] = 1
        grid[2][5] = 1
        grid[1][6] = 1
        grid[0][7] = 1
        if not plt.fignum_exists(display.fig.number):
            break
        display.update_display(grid)
        grid[0][0] = 0
        grid[1][1] = 0 
        grid[2][2] = 0
        grid[3][3] = 0
        grid[4][4] = 0
        grid[5][5] = 0
        grid[6][6] = 0
        grid[7][7] = 0
        grid[7][0] = 0
        grid[6][1] = 0
        grid[5][2] = 0
        grid[4][3] = 0
        grid[3][4] = 0
        grid[2][5] = 0
        grid[1][6] = 0
        grid[0][7] = 0
        if not plt.fignum_exists(display.fig.number):
            break
        display.update_display(grid)
    plt.ioff()