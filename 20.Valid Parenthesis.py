class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={')':'(', '}':'{', ']':'['}
        for char in s:
            if char in d.values():
                stack.append(char)
            else:
                if not stack or stack[-1]!=d[char]:
                    return False
                stack.pop()

        return not stack
            

