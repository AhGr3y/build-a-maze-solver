import time, random

from cell import Cell

class Maze():

    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        # Set seed for reproducible random numbers for debugging
        if self._seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):

        # Loop through _num_cols times
        for i in range(self._num_cols):

            # Initialize empty list to hold filled column
            col = []

            # Loop through _num_rows times
            for j in range(self._num_rows):
                # Initialize cell
                cell = Cell(self._win)
                # Add cell to col
                col.append(cell)

            # Add col to _cells for each column looped
            self._cells.append(col)

        # Loop through _num_cols number of times
        for i in range(self._num_cols):
            # For each column, loop through _num_rows number of times
            for j in range(self._num_rows):
                # Draw a cell for each row
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):

        # Return if there is no window
        if self._win is None:
            return

        # Get top left coordinate of a cell
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        # Get bottom right coordinate of a cell
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        # Draw cell
        self._cells[i][j].draw(x1, y1, x2, y2)
        # Animate the drawing process
        self._animate()

    def _animate(self):

        # Return if there is no window
        if self._win is None:
            return
        
        # Call window's redraw method
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        
        # Get entrance cell (top left)
        entrance_cell = self._cells[0][0]
        # Break left wall of entrance_cell
        entrance_cell.has_top_wall = False
        # Redraw entrance cell
        self._draw_cell(0, 0)

        # Get exit cell (bottom right cell)
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        # Break right wall of exit_cell
        exit_cell.has_bottom_wall = False
        # Redraw exit cell
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):

        # Mark current cell as visited
        self._cells[i][j]._visited = True

        # Loop infinitely
        while True:

            # Create empty list to hold the i and j values you will need to visit
            to_visit = []

            # Check if current cell is at the top of the maze
            if j != 0:
                # Get the top neighbour
                top_neighbour = self._cells[i][j - 1]
                # If top_neighbour has not been visited, add to to_visit list
                if not top_neighbour._visited:
                    to_visit.append((i, j - 1))

            # Check if current cell is at the left most side of the maze
            if i != 0:
                # Get the left neighbour
                left_neighbour = self._cells[i - 1][j]
                # If left_neighbour has not been visited, add to to_visit list
                if not left_neighbour._visited:
                    to_visit.append((i - 1, j))

            # Check if current cell is at the right most side of the maze
            if i != self._num_cols - 1:
                # Get the right neighbour
                right_neighbour = self._cells[i + 1][j]
                # If right_neighbour has not been visited, add to to_visit list
                if not right_neighbour._visited:
                    to_visit.append((i + 1, j))

            # Check if current cell is at the bottom of the maze
            if j != self._num_rows - 1:
                # Get the bottom neighbour
                bottom_neighbour = self._cells[i][j + 1]
                # If bottom_neighbour has not been visited, add to to_visit list
                if not bottom_neighbour._visited:
                    to_visit.append((i, j + 1))

            # If no one to visit, draw the current cell, then return to break out of the loop
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                # Randomly select a neighbour to visit
                next_visit = random.randint(0, len(to_visit) - 1)
                next_i = to_visit[next_visit][0]
                next_j = to_visit[next_visit][1]
                visiting = self._cells[next_i][next_j]

                # Check if visiting is to the top or bottom
                if next_i == i:
                    # If visiting is on the top, knock down wall between visiting and current cell
                    if next_j < j:
                        visiting.has_bottom_wall = False
                        self._cells[i][j].has_top_wall = False
                    # If visiting is on the bottom, knock down wall between visiting and current cell
                    else:
                        visiting.has_top_wall = False
                        self._cells[i][j].has_bottom_wall = False

                # Check if visiting is to the left or right
                if next_j == j:
                    # If visiting is on the left, knock down wall between visiting and current cell
                    if next_i < i:
                        visiting.has_right_wall = False
                        self._cells[i][j].has_left_wall = False
                    # If visiting is on the right, knock down wall between visiting and current cell
                    else:
                        visiting.has_left_wall = False
                        self._cells[i][j].has_right_wall = False

                # Move to visiting
                self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        # Loop through all columns
        for i in range(self._num_cols):
            # Loop through all rows
            for j in range(self._num_rows):
                # Set visited to False
                self._cells[i][j]._visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):

        # Animate any changes
        self._animate()

        # Get current cell
        current_cell = self._cells[i][j]

        # Mark current cell as visited
        current_cell._visited = True

        # Return True if current cell is at the end
        if current_cell == self._cells[self._num_cols - 1][self._num_rows - 1]:
            return True
        
        # If current cell is not at the left-most edge and there is no wall on the left
        if i != 0 and not current_cell.has_left_wall:
            # Get left cell
            left_cell = self._cells[i - 1][j]
            # If left cell not visited
            if not left_cell._visited:
                # Draw red line from current cell to left cell
                current_cell.draw_move(left_cell)
                # Move to left cell, and return True if reach the end
                if self._solve_r(i - 1, j) == True:
                    return True
                else:
                    # Otherwise, draw grey line from current cell to left cell
                    current_cell.draw_move(left_cell, True)
        
        # If current cell is not at the right-most edge and there is no wall on the right
        if i != self._num_cols - 1 and not current_cell.has_right_wall:
            # Get right cell
            right_cell = self._cells[i + 1][j]
            # If right cell not visited
            if not right_cell._visited:
                # Draw red line from current cell to right cell
                current_cell.draw_move(right_cell)
                # Move to right cell, and return True if reach the end
                if self._solve_r(i + 1, j) == True:
                    return True
                else:
                    # Otherwise, draw grey line from current cell to right cell
                    current_cell.draw_move(right_cell, True)

        # If current cell is not at the top-most edge and there is no wall on the top
        if j != 0 and not current_cell.has_top_wall:
            # Get top cell
            top_cell = self._cells[i][j - 1]
            # If top cell not visited
            if not top_cell._visited:
                # Draw red line from current cell to top cell
                current_cell.draw_move(top_cell)
                # Move to top cell, and return True if reach the end
                if self._solve_r(i, j - 1) == True:
                    return True
                else:
                    # Otherwise, draw grey line from current cell to top cell
                    current_cell.draw_move(top_cell, True)

        # If current cell is not at the bottom-most edge and there is no wall on the bottom
        if j != self._num_rows - 1 and not current_cell.has_bottom_wall:
            # Get bottom cell
            bottom_cell = self._cells[i][j + 1]
            # If bottom cell not visited
            if not bottom_cell._visited:
                # Draw red line from current cell to bottom cell
                current_cell.draw_move(bottom_cell)
                # Move to bottom cell, and return True if reach the end
                if self._solve_r(i, j + 1) == True:
                    return True
                else:
                    # Otherwise, draw grey line from current cell to bottom cell
                    current_cell.draw_move(bottom_cell, True)
        
        # If none of the directions worked out, return False
        return False