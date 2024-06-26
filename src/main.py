import random

from graphics import (
    Window,
    Line,
    Point,
)

from maze import Maze

from cell import Cell

def main():
    # Set maze
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created.")

    is_solveable = maze.solve()
    # Print message if maze is solved
    if is_solveable:
        print("Maze is solved!")
    # Print message if maze is not solveable
    else:
        print("Maze is not solveable!")
    win.wait_for_close()

main()