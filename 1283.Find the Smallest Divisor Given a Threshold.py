from math import ceil
def thresholdCalc(arr,div,th) :
    limit = 0

    for i in range(len(arr)) :
        limit += ceil(arr[i] / div)

    if limit <= th :
        return True

    return False

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 1

        while low <= high :
            mid = (low + high) // 2 

            minThreshold = thresholdCalc(nums,mid,threshold)

            if minThreshold :
                ans = mid
                high = mid - 1

            else :
                low = mid + 1

        return ans



        
