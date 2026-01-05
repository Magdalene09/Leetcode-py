from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a = Counter(nums)
        max_c = max(a.values())

        count = 0
        for freq in a.values():
            if freq == max_c:
                count += freq

        return count
