class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []
        word = ''

        for ch in s :

            if stack and ch == stack[-1][1] :
                stack[-1][0] += 1

                if stack[-1][0] == k :
                    stack.pop()

            else : stack.append([1,ch])

        n = len(stack)

        for i in range(n) :
            word += stack[i][0] * stack[i][1]

        return word
