class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        cursum=0
        min_val=float("inf")

        for i in range(n):
            cursum+=nums[i]

            while cursum>=target:
                min_val=min(min_val,i-l+1)
                cursum-=nums[l]
                l+=1
        return 0 if min_val==float("inf") else min_val
            

        
            
