class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        hmap = {0 : 1}

        subCount = 0
        prefixCount = 0

        for i in range(n) :
            rem = nums[i] % 2  
            prefixCount += rem

            if prefixCount - k in hmap :
                subCount += hmap[prefixCount - k]

            hmap[prefixCount] = hmap.get(prefixCount,0) + 1
        
        return subCount
