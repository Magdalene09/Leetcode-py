class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for num in nums:
            if num not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        
        min_key = min(hashmap, key=hashmap.get)
        return min_key
        
        
