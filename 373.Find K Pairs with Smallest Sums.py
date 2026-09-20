import heapq as H

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:

        n = len(nums1)
        m = len(nums2)

        pq = []
        result = []

        count = 0

        for col in range(min(m, k)) :

            H.heappush(pq,[nums1[0] + nums2[col], 0, col])

        while pq and count < k :

            minSum, i, j = H.heappop(pq)
            result.append([nums1[i], nums2[j]])
            count += 1

            if i + 1 < n :
                H.heappush(pq, [nums1[i + 1] + nums2[j], i + 1, j])

        return result
