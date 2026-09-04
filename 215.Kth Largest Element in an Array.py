import heapq as H

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        pq = []

        for num in nums :

            H.heappush(pq, num)

            if len(pq) > k :
                H.heappop(pq)

        return pq[0]
