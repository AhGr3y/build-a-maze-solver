import unittest

from maze import Maze

class Test(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells_large(self):
        num_cols = 30
        num_rows = 40
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        entrance_cell = m1._cells[0][0]
        exit_cell = m1._cells[num_cols - 1][num_rows - 1]
        self.assertEqual(entrance_cell.has_left_wall, False)
        self.assertEqual(exit_cell.has_right_wall, False)

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._reset_cells_visited()
        for col in m1._cells:
            for row in col:
                self.assertEqual(row._visited, False)

if __name__ == "__main__":
    unittest.main()