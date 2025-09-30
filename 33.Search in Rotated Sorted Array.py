class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count=0
        if target not in nums:
            return -1
        for i in range(len(nums)-1):
            if nums[i]==target:
                break
            else:
                count+=1
        return count

        
