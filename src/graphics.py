from tkinter import Tk, BOTH, Canvas

class Window():

    def __init__(self, width, height):  
        # Create root widget
        self._root = Tk()
        # Set title of root widget
        self._root.title("Maze Solver")
        # Create a canvas
        self._canvas = Canvas(self._root, bg="black", height=height, width=width)
        # Pack the canvas so that it's ready to be drawn
        self._canvas.pack(fill=BOTH, expand=1)
        # Create a tracker to keep track of running state
        self.isRunning = False
        # Call close() when windows is closed
        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Updates the display immediately when there are changes to the GUI elements
        self._root.update_idletasks()
        # Process all pending events, such as button clicks or keypresses, and redraw the GUI
        self._root.update()

    def wait_for_close(self):
        self.isRunning = True
        # Redraw the GUI until window is closed
        while self.isRunning:
            self.redraw()
        print("Window closed.")

    def close(self):
        self.isRunning = False

    def draw_line(self, line, fill_color="white"):
        # Draws a colored line on the canvas
        line.draw(self._canvas, fill_color)

class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="white"):
        # Draws a line on the canvas with the given parameters
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)
        # Adjusts the canvas to the parent widget, usually a window
        canvas.pack(fill=BOTH, expand=1)