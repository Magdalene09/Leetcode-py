class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a={}
        b=set()
        for c1,c2 in zip(s,t):
            if c1 in a:
                if a[c1]!=c2:
                    return False
            else:
                if c2 in b:
                    return False
                a[c1]=c2
                b.add(c2)
            
            

        return True
