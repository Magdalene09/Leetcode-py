class Solution:
    def calculate(self, s: str) -> int:

        ans = 0
        num = 0
        sign = 1

        stack = []

        for ch in s :

            if ch.isdigit() : num = num * 10 + int(ch)

            elif ch =='(' :

                stack.append(ans)
                stack.append(sign)

                ans = 0
                sign = 1

            elif ch == '+' :

                ans += sign * num
                num = 0
                sign = 1

            elif ch == '-' :

                ans += sign * num
                num = 0
                sign = -1

            elif ch == ')' :

                ans += sign * num
                num = 0
                sign = 1

                prevSign = stack.pop()
                prevAns = stack.pop()

                ans = prevAns + prevSign * ans

        return ans + sign * num
