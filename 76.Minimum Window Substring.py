from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        n = len(s)
        hmap = {}
        validCount = 0

        req = Counter(t)
        minWinString = ""
        minLength = float("inf")

        left = 0
        right = 0

        while right < n :
            if s[right] in req :
                hmap[s[right]] = hmap.get(s[right], 0) + 1

                if hmap[s[right]] == req[s[right]] :
                    validCount += 1

            while validCount == len(req) :
                if right - left + 1 < minLength :
                    minLength = right - left + 1
                    minWinString = s[left : right+1]

                if s[left] in hmap :
                    hmap[s[left]] -= 1

                    if hmap[s[left]] < req[s[left]] : validCount -= 1
                    if hmap[s[left]] == 0 : del hmap[s[left]]

                left += 1

            right += 1

        return minWinString
