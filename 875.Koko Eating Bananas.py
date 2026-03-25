from math import ceil
def perHour(arr,ph):
    total = 0
    for i in range(len(arr)) :
        total += ceil(arr[i] / ph)

    return total
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = float("inf")
        low = 1
        high = max(piles)

        while low <= high :
            mid = (low + high) // 2
            req_Time = perHour(piles,mid)

            if req_Time <= h :
                min_speed = mid
                high = mid - 1

            else :
                 low = mid + 1

        return min_speed


        
        
