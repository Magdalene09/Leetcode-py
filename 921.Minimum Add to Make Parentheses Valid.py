class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n = len(s)

        openCount = 0
        additional = 0

        for i in range(n) :
            if s[i] == '(' : openCount += 1
            else :
                if openCount > 0 :
                    openCount -= 1

                else : additional += 1

        return openCount + additional
