class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        n = len(s)

        ans = []
        stack = []

        for i in range(n):

            if s[i] == '(' : stack.append(i)

            elif s[i] == ')' :
                if stack and s[stack[-1]] == '(' : stack.pop()
                else : stack.append(i)

            ans.append(s[i])

        while stack :
            ans[stack.pop()] = ''

        return ''.join(ans)
