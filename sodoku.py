
import unittest


class Sudoku:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]

    def set(self, row, col, number):
        self.board[row][col] = number
        self.verifically_row(row, col, number)
        self.verifically_col(row, col, number)
        self.verifically_block(row, col, number)
        
    def verifically_row(self,row,col,number):
            a=0
            for x in range(9):
                if (self.board [x] [col] == number):
                    a +=  1 
                    if a > 1:
                        self.board[row][col] = 0
                        raise Exception()  
    def verifically_col(self,row,col,number):
        b=0
        for y in range(9):
                if (self.board [row] [y] == number):
                    b +=  1 
                    if b > 1:
                        self.board[row][col] = 0
                        raise Exception()
    def verifically_block(self,row,col,number):

        for r in self.row_block(row):
            for c in self.column_block(col):
                if self.board[r][c] == number and r != row and c != col:
                    raise Exception                                                                             
        
        
    def row_block(self,row):
        if (row //3) * 3 == 0:
            return [0,1,2]
        if (row //3) * 3 == 3:
            return[3,4,5]
        if (row //3) * 3 == 6:
            return [6,7,8]

    def column_block(self,column):
        if (column //3) * 3 == 0:
            return  [0,1,2]
        if (column //3) * 3 == 3:
            return  [3,4,5]
        if (column //3) * 3 == 6:
            return  [6,7,8]
   


