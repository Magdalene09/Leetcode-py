class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        range1 = max(1,n - k)
        range2 = n + k
        
        totalSum = 0

        for x in range(range1,range2 + 1) :
            if (n & x) == 0 :
                totalSum += x

        return totalSum
