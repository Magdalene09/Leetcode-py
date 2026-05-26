def sumSequence(arr,length,ind,varSum,target,ds,result) :
    if varSum == target : 
        result.append(ds[:])
        return

    for i in range(ind,length) :
        if i > ind and arr[i] == arr[i-1] : continue
        if arr[i] + varSum > target : break

        ds.append(arr[i])
        sumSequence(arr,length,i + 1,varSum + arr[i],target,ds,result)
        ds.pop()
 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        varSum = 0
        result = []
        ds = []
        candidates.sort()

        sumSequence(candidates,n,0,varSum,target,ds,result)
        return result
