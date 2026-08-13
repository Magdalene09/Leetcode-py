def solveBoard(col, n, board, leftRow, lowerDiag, upperDiag) :

    if col == n :
        return 1

    count = 0
    
    for row in range(n) :

        if leftRow[row] == 0 and upperDiag[(n - 1) + col - row] == 0 and lowerDiag[row + col] == 0 :

            board[row][col] = 'Q'

            leftRow[row] = 1
            upperDiag[(n - 1) + col - row] = 1
            lowerDiag[row + col] = 1

            count += solveBoard(col + 1, n, board, leftRow, lowerDiag, upperDiag)

            board[row][col] = '.'

            leftRow[row] = 0
            upperDiag[(n - 1) + col - row] = 0
            lowerDiag[row + col] = 0

    return count

class Solution:
    def totalNQueens(self, n: int) -> int:

        board = [['.'] * n for _ in range(n)]
        col = 0

        leftRow = [0] * n
        lowerDiag = [0] * (2 * n - 1)
        upperDiag = [0] * (2 * n - 1)

        return solveBoard(col, n, board, leftRow, lowerDiag, upperDiag)
