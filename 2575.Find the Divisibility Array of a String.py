class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        result = [0] * len(word)
        _num = 0

        for i , num in enumerate(word) :
            N = int(num)
            _num = (_num * 10 + N ) % m

            if _num == 0 :
                result[i] = 1


        return result

        
