def daysCheck(arr,weight,days):
    load = 0
    day = 1

    for i in range(len(arr)) :
        if load + arr[i] > weight :
            day += 1
            load = arr[i]

        else :
            load += arr[i]

    if day <= days :
        return True
    
    return False     

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = sum(weights)

        while low <= high :
            mid = (low + high) // 2

            possibleDay = daysCheck(weights,mid,days)

            if possibleDay :
                ans = mid
                high = mid - 1

            else :
                low = mid + 1

        return ans

        
