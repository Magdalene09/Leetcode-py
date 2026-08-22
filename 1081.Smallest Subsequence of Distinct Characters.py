class Solution:
    def smallestSubsequence(self, s: str) -> str:

        n = len(s)
        indexMap = [0] * 26

        for i in range(n) :
            indexMap[ord(s[i]) - ord('a')] = i

        stack = []
        seen = [False] * 26

        for i in range(n) :

            if seen[ord(s[i]) - ord('a')] : continue

            while stack and ord(stack[-1]) >= ord(s[i]) and indexMap[ord(stack[-1])- ord('a')] > i :
                seen[ord(stack[-1]) - ord('a')] = False
                stack.pop()
                
            stack.append(s[i])
            seen[ord(s[i]) - ord('a')] = True

        return ''.join(stack)
