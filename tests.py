import unittest
from sodoku import *
class TestSudoku(unittest.TestCase):
    def test_create_board(self):
        sudoku = Sudoku()
        self.assertEqual(len(sudoku.board), 9)
        self.assertEqual(len(sudoku.board[0]), 9)

    def test_set_number_basic(self):
        sudoku = Sudoku()
        sudoku.set(1, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)

    def test_set_number_validate_column(self):
        sudoku = Sudoku()
        sudoku.set(1, 1, 9)
        with self.assertRaises(Exception):
            sudoku.set(2, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[2][1],0)

    def test_set_number_validate_column_2(self):
        sudoku = Sudoku()
        sudoku.set(1, 1, 9)
        with self.assertRaises(Exception):
            sudoku.set(3, 1, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[3][1],0)

    def test_set_number_validate_row(self):
        sudoku = Sudoku()
        sudoku.set(1, 1, 9)
        with self.assertRaises(Exception):
            sudoku.set(1, 2, 9)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[1][2],0)

    def test_set_number_validate_row_2(self):
        sudoku = Sudoku()
        sudoku.set(1, 1, 9)
        sudoku.set(2,1,8)
        with self.assertRaises(Exception):
            sudoku.set(1, 2, 9)
            sudoku.set(2,7,8)
        self.assertEqual(sudoku.board[1][1], 9)
        self.assertEqual(sudoku.board[2][1], 8)
        self.assertEqual(sudoku.board[1][2],0)
        self.assertEqual(sudoku.board[2][7],0)
    
    def test_numbers_in_the_same_block(self):
        sudoku = Sudoku()
        sudoku.set(1, 1, 9)
        with self.assertRaises(Exception):
            sudoku.set(2, 2, 9)
        self.assertEqual(sudoku.board[1][1], 9)
      

            
        







if __name__ == '__main__':
    unittest.main()