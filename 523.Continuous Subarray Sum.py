class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        hmap = {0 : -1}

        for i , num in enumerate(nums):
            prefix += num

            remainder = prefix if k == 0 else prefix % k

            if remainder in hmap :
                if i - hmap[remainder] >= 2 :
                    return True

            else :
                hmap[remainder] = i

        return False




        
