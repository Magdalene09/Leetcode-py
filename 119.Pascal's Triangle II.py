class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = []
        ans = 1
        lst.append(ans)

        for col in range(1,rowIndex + 1) :
            ans = ans * (rowIndex - col + 1)
            ans = ans // col
            lst.append(ans)

        return lst
        
