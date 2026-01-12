from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_val = float("-inf")
        result = [] 
        a = deque() 
        
        for i in range(len(nums)):
            
            while a and a[0] < i - k + 1:
                a.popleft()
            while a and nums[i] >= nums[a[-1]]:
                a.pop()
            a.append(i)
            if i >= k-1:
                result.append(nums[a[0]])


        return result

