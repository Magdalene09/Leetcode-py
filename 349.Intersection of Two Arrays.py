class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        a = set(nums1)
        for num in nums2  :
            if num in a :
                result.append(num)
                a.remove(num)

        return result
