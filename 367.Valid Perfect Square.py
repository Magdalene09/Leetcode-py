class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0 
        right = num
        while left <= right:
            mid = (right + left) // 2
            squares = mid * mid

            if num == squares : 
                return True
            elif num > squares :
                left = mid + 1
            else : 
                right = mid - 1
        return False
