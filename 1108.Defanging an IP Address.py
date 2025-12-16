class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []
        for num in address :
            if num ==".":
                result.append("[.]")
            else :
                result.append(num)

        return "".join(result)

        
