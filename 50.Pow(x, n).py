class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = abs(n)

        while(nn > 0) :
            if nn % 2 == 1 :
                ans *= x
                nn -= 1
            x *= x
            nn //= 2


        return ans if n >= 0 else 1 / ans



        
