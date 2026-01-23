class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        b = s.split()
        if len(pattern) != len(b):
            return False
        hashmap = {}
        hashmap2 ={}
        
        for p1,s1 in zip(pattern,b):
            if p1 in hashmap and hashmap[p1] != s1:
                return False

            if s1 in hashmap2 and hashmap2[s1] != p1:
                return False

            hashmap[p1]  = s1
            hashmap2[s1] = p1 

        return True
