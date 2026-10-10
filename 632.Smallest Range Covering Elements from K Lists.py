import heapq as H

class Solution:
    def smallestRange(self, nums: list[list[int]]) -> list[int]:

        pq = []
        k = len(nums)

        maxEnd = float("-inf")
        minStart = float("inf")


        for i in range(k) :
            maxEnd = max(maxEnd, nums[i][0])
            minStart = min(minStart, nums[i][0])

            H.heappush(pq, (nums[i][0], i, 0, len(nums[i])))

        ansRange = [minStart, maxEnd] 

        while pq :
            val , li, vi, n = H.heappop(pq)

            if maxEnd - val < ansRange[1] - ansRange[0] :
                ansRange = [val, maxEnd]

            if vi + 1 >= n : break
            
            H.heappush(pq, (nums[li][vi + 1], li, vi + 1, n))
            maxEnd = max(maxEnd, nums[li][vi + 1])

        return ansRange
