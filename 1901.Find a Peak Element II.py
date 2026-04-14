def findIndex(arr,i) :
    ind = 0
    maxElement = float("-inf")

    for x in range(len(arr)) :
        if arr[x][i] > maxElement :
            maxElement = arr[x][i]
            ind = x

    return ind

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1

        while low <= high :
            mid = ( low + high ) // 2

            maxEleIndex = findIndex(mat,mid)
            left =  mat[maxEleIndex][mid - 1] if mid > 0 else -1
            right = mat[maxEleIndex][mid + 1] if mid < m - 1 else -1

            if mat[maxEleIndex][mid] > left and mat[maxEleIndex][mid] > right  :
                return [maxEleIndex,mid]

            
            elif mat[maxEleIndex][mid] < right :
                low = mid + 1

            else :
                high = mid - 1


        return[-1,-1]



                    


