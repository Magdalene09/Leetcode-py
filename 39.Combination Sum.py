def sumSequence(arr,length,ind,ds,result,varSum,target) :
    if varSum == target : 
        result.append(ds[:])
        return

    if ind >= length or varSum > target : return
    
    varSum += arr[ind]
    ds.append(arr[ind])
    sumSequence(arr,length,ind,ds,result,varSum,target)

    varSum -= arr[ind]
    ds.pop()
    sumSequence(arr,length,ind + 1,ds,result,varSum,target)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        varSum = 0
        result = []
        ds = []

        sumSequence(candidates,n,0,ds,result,varSum,target)
        return result
