def findMinVal(h) :
    minVal = float("inf")

    for num in h :
        if num != 0 : minVal = min(minVal, num)

    return minVal

class Solution:
    def beautySum(self, s: str) -> int:

        n = len(s)
        beautySum = 0
        
        for i in range(n) :

            hashArr = [0] * 26
            maxVal = 0
            for j in range(i,n) :

                idx = ord(s[j]) - ord('a')
                hashArr[idx] += 1
                
                maxVal = max(maxVal, hashArr[idx])
                minVal = findMinVal(hashArr)

                beautySum += maxVal - minVal

        return beautySum
