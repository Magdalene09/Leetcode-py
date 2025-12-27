class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        prefix_sum = 0
        count_of_subarray = 0

        for num in nums :
            prefix_sum += num
            if prefix_sum - k in seen :
                count_of_subarray += seen[prefix_sum - k]

            if prefix_sum in seen :
                seen[prefix_sum] += 1
            
            elif prefix_sum not in seen :
                seen[prefix_sum] = 1

        
        return count_of_subarray

            





        
