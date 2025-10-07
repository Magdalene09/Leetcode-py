class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)


        while cur not in seen :
            seen.add(cur)
            summ = 0 
            for val in cur :
                val = int(val)
                summ += val ** 2 
            if summ == 1: return True
            cur = str(summ)

        return False
