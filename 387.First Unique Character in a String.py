from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = Counter(s)
        for i,val in enumerate(s) :
            if a[val] == 1:
                return i
        return -1
