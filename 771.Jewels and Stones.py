class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        numofj=0
        jewels=set(jewels)

        for s in stones:
            if s in jewels:
                numofj+=1
        
        return numofj
        
