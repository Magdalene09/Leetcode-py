class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        m = len(board[0])

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(m)]
        grids = [set() for _ in range(n)]

        for r in range(n) :
            for c in range(m) :
                
                if board[r][c] != '.'  :

                    gIdx = 3 * (r // 3) + c // 3
                    num = int(board[r][c])

                    if num not in rows[r] and num not in cols[c] and num not in grids[gIdx] :

                        rows[r].add(num)
                        cols[c].add(num)
                        grids[gIdx].add(num)

                    else : return False

        return True
