class Solution:
    def numTrees(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        L=[0 for i in range(n+1)]
        L[0]=1
        L[1]=1
        for j in range(2,n+1):
            for k in range(1,j+1):
                L[j]+=L[k-1]*L[j-k]

        return L[n]
