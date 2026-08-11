class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        hashArr1 = [0] * 26
        hashArr2 = [0] * 26

        for ch in s1 :
            idx = ord(ch) - ord('a')
            hashArr1[idx] += 1

        left = 0

        for right in range(m) :
            idx = ord(s2[right]) - ord('a')
            hashArr2[idx] += 1

            if right - left + 1 > n :
                hashArr2[ord(s2[left]) - ord('a')] -= 1
                left += 1

            if hashArr2 == hashArr1 : return True

        return False
