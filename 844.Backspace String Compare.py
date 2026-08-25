class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        n = len(s)
        m = len(t)

        i = n - 1
        j = m - 1

        skip1 = 0
        skip2 = 0

        while i >= 0 or j >= 0 :

            while i >= 0 :

                if s[i] == '#' :
                    skip1 += 1
                    i -= 1
                
                elif skip1 > 0 :
                    skip1 -= 1
                    i -= 1

                else :
                    break

            while j >= 0 : 

                if t[j] == '#' :
                    skip2 += 1
                    j -= 1

                elif skip2 > 0 :
                    skip2 -= 1
                    j -= 1

                else :
                    break

            if i >=0 and j >= 0 :
                if s[i] != t[j] : return False

                i -= 1
                j -= 1

            elif i >= 0 or j >= 0 :
                return False

        return True
