from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums2)

        result = []

        for num in nums1 :
            if a[num] > 0 :
                result.append(num)
                a[num] -= 1

        return result
        
