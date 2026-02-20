class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hmap = {}

        for num in nums :
            if num % 2 == 0 :
                hmap[num] = hmap.get(num,0) + 1

        if not hmap :
            return -1

        result = 0
        max_freq = 0

        for num , freq in hmap.items() :
            if freq > max_freq :
                max_freq = freq
                result = num
            elif freq == max_freq :
                result = min(result,num)

        return result
            
