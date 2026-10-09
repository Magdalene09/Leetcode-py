import heapq as H

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        self.pq = []

        for num in self.nums :

            if len(self.pq) < self.k :
                H.heappush(self.pq, num)
            
            else :

                if self.pq[0] < num :
                    H.heappop(self.pq)
                    H.heappush(self.pq, num)

    def add(self, val: int) -> int:

        if len(self.pq) < self.k :
                H.heappush(self.pq, val)
            
        else :
            
            if self.pq[0] < val :
                H.heappop(self.pq)
                H.heappush(self.pq, val)

        return self.pq[0]
