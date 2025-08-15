from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                new.append(True)
                
            else:
                new.append(False)
                
        
        return new

        
