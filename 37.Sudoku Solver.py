def findSudoku(empty, board, rows, cols, grids, idx) :

    if idx == len(empty) :
        return True

    row, col = empty[idx]
    gIdx = 3 * (row // 3) + col // 3

    for num in range(1,10) :

        if num not in rows[row] and num not in cols[col] and num not in grids[gIdx] :

            board[row][col] = str(num)

            rows[row].add(num)
            cols[col].add(num)
            grids[gIdx].add(num)

            if findSudoku(empty, board, rows, cols, grids, idx + 1) : return True

            board[row][col] = '.'

            rows[row].remove(num)
            cols[col].remove(num)
            grids[gIdx].remove(num)

    return False

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        n = len(board)
        m = len(board[0])

        empty = []

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(m)]
        grids = [set() for _ in range(n)]

        for r in range(n) :
            for c in range(m) :

                if board[r][c] == '.' :
                    empty.append((r,c))

                else :
                    gIdx = 3 * (r // 3) + c // 3
                    num = int(board[r][c])

                    rows[r].add(num)
                    cols[c].add(num)
                    grids[gIdx].add(num)

        findSudoku(empty, board, rows, cols, grids, 0)
