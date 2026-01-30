class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0
        l = 0
        r = 0
        product = 1

        if k <= 1 :
            return 0

        while r < len(nums) :
            product = product * nums[r]

            while product >= k :
                product /= nums[l]
                l += 1

            count += r - l + 1

            r += 1
        
        return count

            
    
        

                

        
