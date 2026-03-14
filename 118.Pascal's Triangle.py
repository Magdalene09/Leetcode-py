def nCr(row):
    lst = []
    ans = 1
    lst.append(ans)
    for col in range(1,row):
        ans = ans * (row - col)
        ans = ans // col
        lst.append(ans)

    return lst

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for row in range(1,numRows+1):
            lst.append(nCr(row))

        return lst
