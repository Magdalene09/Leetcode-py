class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0 
        for i in range(len(nums)):
            nums[i] = nums[i] + summ
            summ = nums[i]
        
        return nums

        
