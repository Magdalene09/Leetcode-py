import heapq as H

class MedianFinder:

    def __init__(self):

        self.maxHeap = []
        self.minHeap = []
    
    def addNum(self, num: int) -> None:

        if not self.maxHeap : H.heappush(self.maxHeap, -num)

        else :
            if num > -self.maxHeap[0] :
                H.heappush(self.minHeap, num)

            else :
                H.heappush(self.maxHeap, -num)

            n = len(self.maxHeap)
            m = len(self.minHeap)
            
            if abs(n - m) > 1 :

                if n > m :
                    val = H.heappop(self.maxHeap)
                    H.heappush(self.minHeap, -val)

                elif n < m :
                    val = H.heappop(self.minHeap)
                    H.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:

        n = len(self.maxHeap)
        m = len(self.minHeap)

        if n == m : return (-self.maxHeap[0] + self.minHeap[0]) / 2
        elif n > m : return -self.maxHeap[0]
        else : return self.minHeap[0]
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
