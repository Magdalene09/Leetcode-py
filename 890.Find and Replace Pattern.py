class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []

        for word in words :
            if len(word)!=len(pattern):
                continue
            hashmap1 = {}
            hashmap2 = {}


            for a1,p1 in zip(word,pattern):
                if a1 in hashmap1 and hashmap1[a1] != p1 :
                    break
                if p1 in hashmap2 and hashmap2[p1] != a1 :
                    break
                hashmap1[a1] = p1
                hashmap2[p1] = a1
            else :
                result.append(word)
    
        return result
