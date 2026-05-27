def sumSequence(ind,varSum,ds,result,target,window):
    if varSum == target and len(ds) == window :
        result.append(ds[:])
        return

    if varSum > target or len(ds) > window :
        return

    for i in range(ind,10) :
        varSum += i
        ds.append(i)
        sumSequence(i + 1,varSum,ds,result,target,window)

        varSum -= i
        ds.pop()

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        varSum = 0
        ds = []
        result = []
        sumSequence(1,varSum,ds,result,n,k)

        return result
