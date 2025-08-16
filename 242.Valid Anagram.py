
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        oned={}
        twod={}
        for i in s.lower():
            if i in oned:
                oned[i]+=1
            else:
                oned[i]=1
        for j in t.lower():
            if j in twod:
                twod[j]+=1
            else:
                twod[j]=1
        return oned==twod
