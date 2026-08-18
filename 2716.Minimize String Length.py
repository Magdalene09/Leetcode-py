class Solution:
    def minimizedStringLength(self, s: str) -> int:

        hashArr = [0] * 26
        length = 0

        for ch in s :

            idx = ord(ch) - ord('a')
            if hashArr[idx] == 0 : 
                length +=1
                hashArr[idx] = 1

        return length
