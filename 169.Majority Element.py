class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        MajE=None
        for num in nums:
            if count==0:
                MajE=num
            if num==MajE:
                count+=1
            else:
                count-=1

        return MajE
                  
