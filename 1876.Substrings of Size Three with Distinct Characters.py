class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
    
        for i in range(len(s)-2) :
            a = s[i]
            b = s[i+1]
            c = s[i+2]

            if a != b and b != c and c != a :
                count +=1

        return count


or 

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        a = set()

        l = 0 
        r = 0
        n = len(s)

        while r < n :
            while s[r] in a :
                a.remove(s[l])
                l += 1

            a.add(s[r])

            if r - l + 1 == 3 :
                count += 1
                a.remove(s[l])
                l += 1

            r += 1

        return count
