def allsubSequence(arr,length,ind,ds,result) :
    result.append(ds[:])
        
    for i in range(ind,length) :
        if i > ind and arr[i] == arr[i-1] : continue
        ds.append(arr[i])
        allsubSequence(arr,length,i+1,ds,result)
        ds.pop()
        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ds = []
        result = []
        n = len(nums)
        nums.sort()
        allsubSequence(nums,n,0,ds,result)

        return result
