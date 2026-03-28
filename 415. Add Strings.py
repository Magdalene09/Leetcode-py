class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        '''return str(int(num1)+int(num2))'''

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry :

            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            s = d1 + d2 + carry
            result.append(str(s % 10))
            carry = s // 10

            i -= 1
            j -= 1

        return "".join(result[::-1])


 









        
