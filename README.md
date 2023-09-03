# MazeSolver
This repo is part from a personal project to improve my troubleshooting skills.
It has various ways of solving a maze in Python and one of them in Assembly.

## Python Version

To run this project you will need to install the follow libraries:
* Numpy
* Pandas
* Opencv2

After installing the deppendences, all you need is to import the MazeSolver object.
You can also import the Plot and Timer libraries if you want to compare the execution time.
The image input must be 1px thick between the walls and possible paths. 

MazeSolver object parameters:
* IMG_PATH = Maze .png file
* POSSIBLE_PATH = Possible path color (GRAYSCALE)
* EXIT = Maze exits color (GRAYSCALE)
* WALL = Wall color (GRAYSCALE)
* DEAD_END_WALL = Dead end color (GRAYSCALE)
* (Optional) Generates the imgs for the video creation

The function **solve** has 3 different algorithms to solve the maze:
* up_down -> apply the dead-end-algorithm starting the iteration only from up-left to down-right.
* rotation -> rotates the iteration method between starting from the 4 edges.
* random_rotation -> randomily choose which interation method. 
* agent -> create one agent object in each dead-end.

### Example:

```python
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
```

## Assembly Version

The assembly version was made using the Mars4_5.jar, and receives as input a .pgm image.

```assembly
arquivo: .asciiz "maze-1-2.pgm"           # Nome do arquivo a ser lido
nome_arquivo: .asciiz "Solucao.pgm"       # Nome do arquivo a ser escrito 
```

## Output Examples:



https://github.com/JCGCosta/MazeSolver/assets/51680369/65fc81df-9f7b-4c30-8990-1cc6f87b78d0



https://github.com/JCGCosta/MazeSolver/assets/51680369/1000c415-7563-4f55-ace0-d20ec9719bf5



<img src="https://github.com/JCGCosta/MazeSolver/blob/main/src/Python/solutions/imgs/maze301x301_36502_solved.png?raw=true" alt="301x301MazeSolution" title="Output solution example.">
