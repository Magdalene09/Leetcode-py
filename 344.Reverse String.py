class Solution:
    def reverseString(self, s: List[str]) -> None:
        lp=0
        rp=len(s)-1
        while lp<rp:
            s[lp],s[rp]=s[rp],s[lp]


            lp+=1
            rp-=1    

        return s   

#or
class Solution:
    def reverseString(self, s: List[str]) -> None:
        return s.reverse()
