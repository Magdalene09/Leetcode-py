class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        result = []
        depth = 0

        for ch in s :
            if ch == '(' : 
                depth += 1

                if depth > 1 :
                    result.append(ch)

            else :
                if depth > 1 : 
                    result.append(ch)

                depth -= 1
    
        return "".join(result)
