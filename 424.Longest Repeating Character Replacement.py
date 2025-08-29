class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        hashmap={}
        maxlen=0
        for right in range(len(s)):
            hashmap[s[right]]=hashmap.get(s[right],0)+1
            freq=max(hashmap.values())
            if right-left+1-freq>k:
                hashmap[s[left]]-=1
                left+=1
            maxlen=max(maxlen,right-left+1)

        return maxlen

   
