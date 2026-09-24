class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        hashArr = [False] * 26
        count = 0

        for ch in sentence :

            index = ord(ch) - ord('a')

            if not hashArr[index] :
                hashArr[index] = True
                count += 1

        return count == 26
