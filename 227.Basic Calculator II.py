class Solution:
    def calculate(self, s: str) -> int:

        n = len(s)

        numStack = []
        ops = '+'

        num = 0

        for i in range(n + 1) :

            ch = '+' if i == len(s) else s[i]

            if ch.isdigit() :
                num = num * 10 + int(ch)

            elif ch != ' ' :
                op = ch

                if ops == '+' :
                    numStack.append(num)

                elif ops == '-' :
                    numStack.append(-num)

                elif ops == '*' :
                    top = numStack.pop()
                    numStack.append(top * num)

                else :
                    top = numStack.pop()
                    numStack.append(int(top / num))

                ops = op
                num = 0

        ans = 0
        while numStack :
            ans += numStack.pop()

        return ans
