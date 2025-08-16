class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=0
        l=len(nums)-1    
        while k<=l:
            mid=(k+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                k=mid+1
            else:
                l=mid-1
        return k



     
