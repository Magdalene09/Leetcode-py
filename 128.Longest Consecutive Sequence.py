class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        a = set(nums)
        count = 0
        max_c = float("-inf")
        for num in a :
            if num - 1 not in a  :
                count = 1
                current = num

                while current + 1 in a :
                    count += 1
                    current += 1

            max_c = max(max_c,count)

        
        return max_c

