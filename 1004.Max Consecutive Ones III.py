class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        l = 0
        r = 0
        count1 = 0
        
        while r < len(nums) :
            if nums[r] == 1 :
                count1 += 1


            if r - l + 1 - count1 > k :
                if nums[l] == 1 :
                    count1 -= 1
                l += 1
                

            max_len = max(max_len , r-l+1)

            r += 1
        return max_len
