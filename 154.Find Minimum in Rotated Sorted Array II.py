class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        minVal = float("inf")

        while low <= high :
            mid = ( low + high ) // 2

            if nums[mid] == nums[low] == nums[high] :
                minVal = min(minVal,nums[low])
                low += 1
                high -= 1
                continue

            if nums[low] < nums[high] :
                minVal = min(minVal,nums[low])
                break

            if nums[low] <= nums[mid] :
                minVal = min(minVal,nums[low])
                low = mid + 1

            else :
                minVal = min(minVal,nums[mid])
                high = mid - 1

        return minVal
        
