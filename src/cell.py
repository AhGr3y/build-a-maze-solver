from graphics import (
    Point,
    Line,
)

class Cell():

    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self._visited = False

    def draw(self, x1, y1, x2, y2):

        # If window does not exist, return
        if self._win is None:
            return

        # Set coordinates
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        # Create a point for each corner of the cell
        top_left_p = Point(self._x1, self._y1)
        top_right_p = Point(self._x2, self._y1)
        bottom_left_p = Point(self._x1, self._y2)
        bottom_right_p = Point(self._x2, self._y2)
        
        # Initialize background color
        background_color = "black"

        # If cell has top wall, draw a top wall
        if self.has_top_wall:
            line = Line(top_left_p, top_right_p)
            self._win.draw_line(line)
        # If cell does not have top wall, draw a wall with same color as background
        elif not self.has_top_wall:
            line = Line(top_left_p, top_right_p)
            self._win.draw_line(line, background_color)

        # If cell has right wall, draw a right wall
        if self.has_right_wall:
            line = Line(top_right_p, bottom_right_p)
            self._win.draw_line(line)
        # If cell does not have right wall, draw a wall with same color as background
        elif not self.has_right_wall:
            line = Line(top_right_p, bottom_right_p)
            self._win.draw_line(line, background_color)

        # If cell has bottom wall, draw a bottom wall
        if self.has_bottom_wall:
            line = Line(bottom_left_p, bottom_right_p)
            self._win.draw_line(line)
        # If cell does not have bottom wall, draw a wall with same color as background
        elif not self.has_bottom_wall:
            line = Line(bottom_left_p, bottom_right_p)
            self._win.draw_line(line, background_color)

        # If cell has left wall, draw a left wall
        if self.has_left_wall:
            line = Line(top_left_p, bottom_left_p)
            self._win.draw_line(line)
        # If cell does not have left wall, draw a wall with same color as background
        elif not self.has_left_wall:
            line = Line(top_left_p, bottom_left_p)
            self._win.draw_line(line, background_color)

    def draw_move(self, to_cell, undo=False):

        # If window does not exist, return
        if self._win is None:
            return
        
        # If undo is False, draw a red line
        fill_color = "red"
        # If undo is True, draw a grey line
        if undo:
            fill_color = "grey"
        
        # Get center coordinates of current cell
        current_center_x = (self._x1 + self._x2) / 2
        current_center_y = (self._y1 + self._y2) / 2
        # Get center point of current cell
        current_center_point = Point(current_center_x, current_center_y)

        # Get center coordinates of to_cell
        to_center_x = (to_cell._x1 + to_cell._x2) / 2
        to_center_y = (to_cell._y1 + to_cell._y2) / 2
        # Get center point of to_cell
        to_center_point = Point(to_center_x, to_center_y)

        # Move left
        if self._x1 > to_cell._x1:

            # Get center-left point of current cell
            current_center_left_point = Point(self._x1, current_center_y)
            # Get line from current center to current center-left
            line = Line(current_center_left_point, current_center_point)
            # Draw line from current center to current center-left
            self._win.draw_line(line, fill_color)

            # Get center-right point of to_cell
            to_center_right_point = Point(to_cell._x2, to_center_y)
            # Get line from to_cell center to to_cell center-right
            line = Line(to_center_point, to_center_right_point)
            # Draw line from to_cell center to to_cell center-right
            self._win.draw_line(line, fill_color)

        # Move right
        if self._x1 < to_cell._x1:

            # Get center-right point of current cell
            current_center_right_point = Point(self._x2, current_center_y)
            # Get line from current center to current center-right
            line = Line(current_center_point, current_center_right_point)
            # Draw line from current center to current center-right
            self._win.draw_line(line, fill_color)

            # Get center-left point of to_cell
            to_center_left_point = Point(to_cell._x1, to_center_y)
            # Get line from to_cell center to to_cell center-left
            line = Line(to_center_point, to_center_left_point)
            # Draw line from to_cell center to to_cell center-left
            self._win.draw_line(line, fill_color)

        # Move to top
        if self._y1 > to_cell._y1:

            # Get center-top point of current cell
            current_center_top_point = Point(current_center_x, self._y1)
            # Get line from current center to current center-top
            line = Line(current_center_point, current_center_top_point)
            # Draw line from current center to current center-top
            self._win.draw_line(line, fill_color)

            # Get center-bottom point of to_cell
            to_center_bottom_point = Point(to_center_x, to_cell._y2)
            # Get line from to_cell center to to_cell center-bottom
            line = Line(to_center_point, to_center_bottom_point)
            # Draw line from to_cell center to to_cell center-bottom
            self._win.draw_line(line, fill_color)

        # Move to bottom
        if self._y1 < to_cell._y1:

            # Get center-bottom point of current cell
            current_center_bottom_point = Point(current_center_x, self._y2)
            # Get line from current center to current center-bottom
            line = Line(current_center_point, current_center_bottom_point)
            # Draw line from current center to current center-bottom
            self._win.draw_line(line, fill_color)

            # Get center-top point of to_cell
            to_center_top_point = Point(to_center_x, to_cell._y1)
            # Get line from to_cell center to to_cell center-top
            line = Line(to_center_point, to_center_top_point)
            # Draw line from to_cell center to to_cell center-top
            self._win.draw_line(line, fill_color)