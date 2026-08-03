class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []

        for i in range(n) :
            cIndex = abs(nums[i]) - 1

            if nums[cIndex] < 0 : result.append(abs(nums[i]))
            else : nums[cIndex] *= -1

        return result    
