class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = 0
        hashmap = {0 : -1}
        max_len = 0

        for i in range(len(nums)) :
            if nums[i] == 0 :
                prefix += -1
            
            else :
                prefix += 1


            if prefix in hashmap :
                max_len = max(max_len,i - hashmap[prefix])
            
            else :
                hashmap[prefix] = i


        return max_len

        
        
