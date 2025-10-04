class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        Val = Counter(nums)

        for frequency in Val.values():
            if frequency > 2 :
                return False
        return True
        
