class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        n = len(word1)
        m = len(word2)

        i = s1 = 0
        j = s2 = 0

        while i < n and j < m :

            if word1[i][s1] != word2[j][s2] : return False

            s1 += 1
            s2 += 1

            if s1 == len(word1[i]) :
                i += 1
                s1 = 0

            if s2 == len(word2[j]) :
                j += 1
                s2 = 0

        return i == n and j == m
