def findkCount(mat,target) :
    n = len(mat)
    row = n - 1
    col = 0
    count = 0
    
    while row >= 0 and col < n :
        if target < mat[row][col] :
            row -= 1
            
        else :
            count += row + 1
            col += 1
            
    return count

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        while low <= high :
            mid = ( low + high ) // 2
            kCount = findkCount(matrix,mid)
            
            if kCount >= k :
                high = mid - 1
                
            else :
                low = mid + 1
                
                
        return low
        
