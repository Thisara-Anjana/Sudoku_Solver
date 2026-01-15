import numpy as np

sudoku_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def possibility(Row,Column,Num):
    global sudoku_puzzle
    for i in range(0, 9):
        if sudoku_puzzle[Row][i] == Num:
            return False
        

    for i in range(0, 9):
        if sudoku_puzzle[i][Column] == Num:
            return False
        

    x = (Column // 3) * 3
    y = (Row // 3) * 3 

    for i in range(0,3):
        for j in range(0,3):
            if sudoku_puzzle[y + i][x + j] == Num:
                return False
            
    return True


def solve():
    global sudoku_puzzle
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_puzzle[i][j] == 0:
                for k in range(1, 10):
                    if possibility(i, j, k):
                        sudoku_puzzle[i][j] = k
                        solve()
                        sudoku_puzzle[i][j] = 0
                return
    print(np.matrix(sudoku_puzzle)) 

    input("More solutions?")
solve()
