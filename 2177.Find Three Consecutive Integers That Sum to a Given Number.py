class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0 :
            return []

        div = num // 3
        return [div-1,div,div+1]
        
