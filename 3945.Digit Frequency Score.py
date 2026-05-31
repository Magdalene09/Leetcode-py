class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        if n == 0 :
            return 0
        
        freqScore = 0

        while n > 0 :
            number = n % 10
            freqScore += number
            n //= 10
        
        return freqScore
