class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        if n == k : return sum(cardPoints)

        lScore = 0
        rScore = 0

        for i in range(k) :
            lScore += cardPoints[i]

        maxScore = lScore
        rInd = n - 1

        for i in range(k-1,-1,-1) :
            lScore -= cardPoints[i]
            rScore += cardPoints[rInd]

            maxScore = max(rScore + lScore,maxScore)
            rInd -= 1

        return maxScore
