class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_count = max(special[0] - bottom , top - special[-1])

        for i in range(1,len(special)) :
            max_count = max(max_count,special[i] - special[i-1] -  1)

        return max_count
       
            


        
