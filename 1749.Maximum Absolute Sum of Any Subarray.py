class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        pos_sum = 0
        neg_sum = 0

        for r in range(len(nums)):
            pos_sum += nums[r]
            max_sum = max(max_sum,pos_sum)

            if pos_sum < 0 :
                pos_sum = 0

            neg_sum += nums[r]
            min_sum = min(min_sum,neg_sum)

            if neg_sum > 0 :
                neg_sum = 0


        return max(max_sum,abs(min_sum))
