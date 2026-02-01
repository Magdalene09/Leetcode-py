class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_sum = 0
        summ = 0
        a = set()

        while r < len(nums) :
            while nums[r] in a :
                a.remove(nums[l])
                summ -= nums[l]
                l += 1
            
            summ += nums[r]
            a.add(nums[r])

            if r - l + 1 > k :
                summ -= nums[l]
                a.remove(nums[l])
                l += 1

            if r - l + 1 == k :
                max_sum = max(max_sum,summ)

            r += 1


        return max_sum
        
