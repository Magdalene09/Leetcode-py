class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.noRows = len(matrix) + 1
        self.noCols = len(matrix[0]) + 1

        self.prefixMat = [[0] * self.noCols  for _ in range(self.noRows)]

        for i in range(1,self.noRows) :
            for j in range(1,self.noCols) :

                self.prefixMat[i][j] = matrix[i - 1][j - 1] + self.prefixMat[i - 1][j] + self.prefixMat[i][j - 1] - self.prefixMat[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        topLeft = self.prefixMat[row1][col1] 
        top = self.prefixMat[row1][col2 + 1]
        left = self.prefixMat[row2 + 1][col1]
        total = self.prefixMat[row2 + 1][col2 + 1]

        return total - (top + left) + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
