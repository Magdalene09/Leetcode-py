class Solution:
    def minMoves(self, nums: List[int]) -> int:

        if not nums : return 0

        n = len(nums)
        max_element = max(nums)
        moves = 0

        for i in range(n) :
            moves += max_element - nums[i]

        return moves
