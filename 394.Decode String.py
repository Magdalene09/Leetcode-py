class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:

            if ch.isdigit() or ch.isalpha() or ch == '[':
                stack.append(ch)

            else:

                sb = []

                while stack[-1] != '[':
                    sb.append(stack.pop())

                stack.pop()

                db = []

                while stack and stack[-1].isdigit():
                    db.append(stack.pop())

                db.reverse()
                sb.reverse()

                stack.append(''.join(sb) * int(''.join(db)))

        return ''.join(stack)
