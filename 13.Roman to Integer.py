class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {'I' : 1 , 'V' : 5, 'X' : 10 , 'L' : 50 , 'C' : 100 , 'D' : 500 , 'M' : 1000}
        Num = 0
        prev = 0
        
        for i in range(len(s)-1,-1,-1) :
            val = hmap[s[i]]

            if prev > val :
                Num -= val

            else : 
                Num += val

            prev = val

        return Num

            
            

        
