class Solution:
    def reverseVowels(self, s: str) -> str:
        Vow= ['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U']
        l=list(s)
        lp=0
        rp=len(l)-1
        while lp<rp:
            if l[lp].lower() not in Vow:
                lp+=1
            
            elif l[rp].lower() not in Vow:
                rp-=1

            else:
                l[lp],l[rp]=l[rp],l[lp]
                lp+=1
                rp-=1

        return "".join(l)
        

        
        
