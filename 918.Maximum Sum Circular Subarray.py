class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = nums[0]

        curMax = nums[0]
        globalMax = nums[0]
        curMin = nums[0]
        globalMin = nums[0]

        for num in nums[1:] :
            total += num

            curMax = max(num,curMax+num)
            globalMax = max(curMax,globalMax)

            curMin = min(num,curMin+num)
            globalMin = min(curMin,globalMin)



        if globalMax < 0 :
            return globalMax

            
        return max(globalMax,total - globalMin)



        

        

         
