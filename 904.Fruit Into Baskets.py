class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        Count = 0
        hmap = {}
        l = 0

        for i in range(len(fruits)) :
            hmap[fruits[i]] = hmap.get(fruits[i],0) + 1

            while len(hmap) > 2 :
                hmap[fruits[l]] -= 1
                if hmap[fruits[l]] == 0:
                    del hmap[fruits[l]]
                l += 1

            Count = max(Count,i - l + 1)

        return Count

        
