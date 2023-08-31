import MazeSolver
import matplotlib.pyplot as plt

class Plot:
    def __init__(self, MAZE_SOLVER):
        self.MAZE_SOLVER = MAZE_SOLVER

    def add_plot_line(self):
        plt.plot(self.MAZE_SOLVER.EXIT_FILLED_LIST, label=self.MAZE_SOLVER.CURRENT_SOLUTION_MODE)

    def show(self):
        plt.legend()
        plt.show()