import matplotlib as mpl
import matplotlib.pyplot as plt

class DisplayGrid:
    """Class to handle the display of cell grid using matplotlib."""
    def __init__(self, grid):
        """Initialize the DisplayGrid with a grid and set up the matplotlib figure and axes."""
        self.grid = grid
        self.fig, self.ax = plt.subplots()
        self.color_map = mpl.colors.ListedColormap(['black', 'white'])  # Black for dead cells, white for alive cells
        self.im = None
        plt.ion()  # Turn on interactive mode
        self.fig.canvas.mpl_connect('key_press_event', self.on_press) # Connect key press event to the on_press method
        self.fig.canvas.mpl_connect('button_press_event', self.on_click) # Connect mouse click event to the on_click method
        self.is_running = True  # Flag to control the main loop

    def display(self):
        """Create a visual representation of the grid using matplotlib."""
        self.im = self.ax.imshow(self.grid, cmap=self.color_map, 
                                 interpolation='nearest', vmin=0, vmax=1)
        plt.xticks([])  # Remove x-axis ticks
        plt.yticks([])  # Remove y-axis ticks
        self.ax.set_title("Press space to pause, q to quit")
        plt.show(block=False)  # Non-blocking show to allow updates
        plt.pause(0.1)  # Pause to allow the plot to render

    def update_display(self, new_grid):
        """Update the display with a new grid state."""
        self.grid = new_grid
        self.im.set_data(self.grid)
        plt.draw()
        plt.pause(0.5)


    def on_press(self, event):
        """Handle key press events to control the simulation."""
        if event.key == ' ':
            self.is_running = not self.is_running  # Toggle the running state
            if self.is_running:
                self.ax.set_title("Press space to pause, q to quit")
            else:
                self.ax.set_title("Press space to resume, q to quit\nClick any cell to toggle its state")
        elif event.key == 'q':
            self.is_running = False  # Stop the main loop
            plt.close(self.fig)  # Close the figure window

    def on_click(self, event):
        """Handle mouse click events to toggle cell states."""
        if not self.is_running:
            if event.inaxes is not None:
                x, y = round(event.xdata), round(event.ydata)
                if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid):
                    self.grid[y][x] = not self.grid[y][x]  # Toggle cell state
                    self.update_display(self.grid)  # Update the display with the new grid state

    def control_main_loop(self, grid, next_generation, delay=0.1):
        """Control the main loop of the simulation, allowing for updates and user interaction."""
        plt.ion()
        self.grid = grid
        self.display()

        while plt.fignum_exists(self.fig.number):
            if self.is_running:
                self.grid = next_generation() # Get next generation
                self.update_display(self.grid) # Update display w/ next generation
            
            plt.pause(delay)

    def next_generation(self, grid):
        """Example next generation function that toggles specific cells in the grid."""
        grid[0][0] = not grid[0][0]
        grid[1][1] = not grid[1][1]
        grid[2][2] = not grid[2][2]
        grid[3][3] = not grid[3][3]
        grid[4][4] = not grid[4][4]
        grid[5][5] = not grid[5][5]
        grid[6][6] = not grid[6][6]
        grid[7][7] = not grid[7][7]
        grid[7][0] = not grid[7][0]
        grid[6][1] = not grid[6][1]
        grid[5][2] = not grid[5][2]
        grid[4][3] = not grid[4][3]
        grid[3][4] = not grid[3][4]
        grid[2][5] = not grid[2][5]
        grid[1][6] = not grid[1][6]
        grid[0][7] = not grid[0][7]
        return grid  # Return the updated grid




if __name__ == "__main__":
    # Example usage
    rows, cols = 8, 8
    grid = [[0 for _ in range(cols)] for _ in range(rows)]  
    display = DisplayGrid(grid)
    display.display()
    display.control_main_loop(grid, display.next_generation, delay=0.5)