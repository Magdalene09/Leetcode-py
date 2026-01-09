class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = 1
        suffix = 1
        max_p = float("-inf")

        for i in range(N):
            if prefix == 0 :
                prefix = 1

            if suffix == 0 :
                suffix = 1

            
            prefix = prefix * nums[i]
            suffix = suffix * nums[N-i-1]
            max_p = max(max_p,prefix,suffix)

        return max_p

        
