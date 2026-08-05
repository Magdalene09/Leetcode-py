class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)

        left = 0
        right = 0
        curSum = 0
        maxFreq = 0

        while right < n :

            curSum += nums[right]
            window = right - left + 1

            while curSum + k < nums[right] * window :
                curSum -= nums[left]
                left += 1
                window -= 1

            if curSum + k >= nums[right] * window :
                maxFreq = max(maxFreq, window)
                
            right += 1

        return maxFreq
