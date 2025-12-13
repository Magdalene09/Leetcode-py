class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = []
        count = 0
        for sentence in sentences :
            a = sentence.split()
            result.append(len(a))
        return max(result)
