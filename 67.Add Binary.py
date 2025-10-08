class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a , 2)
        b = int(b , 2)

        while b :
            without_c = a ^ b
            with_c = (a & b) << 1
            a,b = without_c,with_c

        return bin(a)[2:] 
