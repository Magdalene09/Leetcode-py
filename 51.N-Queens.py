def solveBoard(board, col, n, result, leftRow, lowerDiag, upperDiag) :

    if col == n :
        temp = []
         
        for row in range(n) :
            temp.append("".join(board[row]))
        
        result.append(temp)
        return

    for row in range(n) :

        if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[(n - 1) + col - row] == 0 :
            board[row][col] = 'Q'

            leftRow[row] = 1
            lowerDiag[row + col] = 1
            upperDiag[(n - 1) + col - row] = 1

            solveBoard(board, col + 1, n, result, leftRow, lowerDiag, upperDiag)

            board[row][col] = '.'
            leftRow[row] = 0
            lowerDiag[row + col] = 0
            upperDiag[(n - 1) + col - row] = 0

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        result = []
        col = 0
        
        leftRow = [0] * n
        lowerDiag = [0] * (2 * n - 1)
        upperDiag = [0] * (2 * n - 1)

        solveBoard(board, col, n, result, leftRow, lowerDiag, upperDiag)
        return result
        
