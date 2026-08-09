class Solution:
    def maxDepth(self, s: str) -> int:

        n = len(s)
        maxDepth = 0
        depth = 0

        for i in range(n) :

            if s[i] == '(' : depth += 1
            elif s[i] == ')' : depth -= 1

            maxDepth = max(maxDepth, depth)

        return maxDepth
