class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        remainder_seen = {0:1}
        
        for num in nums :
            prefix_sum += num 
            remainder = prefix_sum % k

            if remainder in remainder_seen :
                count += remainder_seen[remainder]
                remainder_seen[remainder] += 1
            
            else :
                remainder_seen[remainder] = 1
        
        return count
                


        
