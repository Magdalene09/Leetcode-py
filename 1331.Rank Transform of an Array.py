class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        rankMap = {}
        result = []

        a = arr[:]
        
        a.sort()
        rank = 1

        for i in range(len(a)) :

            if a[i] not in rankMap :
                rankMap[a[i]] = rank
                rank += 1
 
        for num in arr :
            result.append(rankMap[num])

        return result
