class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        lp=0
        for rp in range(1,len(nums)):
            if nums[lp]!=nums[rp]:
                lp+=1
                nums[lp]=nums[rp]
        
        return lp+1

        
