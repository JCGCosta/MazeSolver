import MazeSolver
import Plot
import Timer

mazeSolver = MazeSolver.MazeSolver("maze41x41.png", 255, 127, 0, 50, True)
plot = Plot.Plot(mazeSolver)

timer = Timer.Timer()
mazeSolver.solve("rotation")
timer.stop()
plot.add_plot_line()
mazeSolver.save_solution_video("temp_imgs/", "solutions/videos/", 120)
mazeSolver.save_solution("solutions/imgs/")

plot.show()