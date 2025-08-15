class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        letters=['a', 'e', 'i', 'o','u']
        count=0
        lp=0
        result=0
        for i in range(len(s)):
            count+=1 if s[i] in letters else 0
            if i-lp+1>k:
                count-=1 if s[lp] in letters else 0
                lp+=1
            result=max(count,result)
        return result



