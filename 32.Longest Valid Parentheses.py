class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        maxLength = 0

        leftB = 0
        rightB = 0
        
        for i in range(n) :

            if s[i] == '(' : leftB += 1
            else : rightB += 1

            if leftB == rightB : 
                maxLength = max(maxLength, 2 * leftB)

            elif rightB > leftB :
                rightB = leftB = 0

        leftB = 0
        rightB = 0

        for i in range(n - 1, -1, -1) :

            if s[i] == '(' : leftB += 1
            else : rightB += 1

            if leftB == rightB : 
                maxLength = max(maxLength, 2 * leftB)

            elif rightB < leftB :
                rightB = leftB = 0

        return maxLength
