from math import ceil
def minSpeed(arr,speed,totalhrs) :
    hrs = 0
    for i in range(len(arr)-1) :
        hrs += ceil(arr[i] / speed)

        if hrs > totalhrs :
            return False
    
    hrs += arr[-1] / speed
    return hrs <= totalhrs

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low = 1
        high = 10 ** 7
        ans = -1

        while low <= high :
            mid = (low + high) // 2

            speed = minSpeed(dist,mid,hour)

            if speed : 
                ans = mid
                high = mid - 1

            else :
                low = mid + 1

        return ans

        

        
