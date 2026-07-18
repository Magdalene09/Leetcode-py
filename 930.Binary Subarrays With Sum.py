class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        n = len(nums)
        
        subCounts = 0
        prefixSum = 0
        hmap = {0 : 1}

        for i in range(n) :
            prefixSum += nums[i]

            if prefixSum - goal in hmap :
                subCounts += hmap[prefixSum - goal]

            hmap[prefixSum] = hmap.get(prefixSum, 0) + 1

        return subCounts
