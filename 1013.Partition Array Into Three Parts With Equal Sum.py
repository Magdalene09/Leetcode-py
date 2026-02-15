class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        Total = sum(arr)

        if Total % 3 != 0 :
            return False

        prefix = 0
        count = 0

        for num in arr :
            prefix += num

            if prefix == Total // 3 :
                count += 1
                prefix = 0 

        
        return count >= 3



        
