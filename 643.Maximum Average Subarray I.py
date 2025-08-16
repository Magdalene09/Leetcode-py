class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cursum=0
        for i in range(k):
            cursum+=nums[i]

        maxi=cursum/k

        for i in range(k,len(nums)):
            cursum+=nums[i]
            cursum-=nums[i-k]

            avg=cursum/k
            maxi=max(maxi,avg)

        return maxi
        
