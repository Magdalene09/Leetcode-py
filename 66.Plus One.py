class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a=int(''.join(map(str,digits)))
        b=a+1
        c=list(map(int,str(b)))
        return c
    

        
        
