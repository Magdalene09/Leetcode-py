class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        n = len(s)
        hashArr = [-1,-1,-1]

        validSubCount = 0

        for i in range(n) :
            hashArr[ord(s[i]) - ord('a')] = i

            if hashArr[0] != -1 and hashArr[1] != -1 and hashArr[2] != -1 : #no need to write if as it gets automatcally cancelled out by targeting the minimum val 
                validSubCount += 1 + min(hashArr[0],hashArr[1],hashArr[2])

        return validSubCount
