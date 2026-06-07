def binarySubstrings(ch, index, cost, length, result, limit) :
    if index == length and cost <= limit :
        result.append(ch)
        return

    if cost > limit : return

    binarySubstrings(ch + '0', index + 1, cost, length, result, limit)
    if not ch or ch[-1] != '1' : binarySubstrings(ch + '1', index + 1, cost + index, length, result, limit)
        

class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        result = []
        binarySubstrings("", 0, 0, n, result, k)
        return result
