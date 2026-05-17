def upperBound(r,k) :
    low = 0
    high = r

    while low <= high :
        mid = ( low + high ) // 2 

        if mid ** k > r :
            high = mid - 1

        else :
            low = mid + 1

    return low
    
def lowerBound(l,k) :
    low = 0
    high = l

    while low <= high :
        mid = ( low + high ) // 2 

        if mid ** k >= l :
            high = mid - 1

        else :
            low = mid + 1

    return low

class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        return upperBound(r,k) - lowerBound(l,k)
