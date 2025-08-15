class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index,value in enumerate(nums):
            desired=target-value
            if desired in hashmap:
                return[index,hashmap[desired]]
            hashmap[value]=index
            
           
        
