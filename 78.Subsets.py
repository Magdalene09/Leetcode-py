def allsubSequence(arr,length,ind,ds,result) :
    result.append(ds[:])

    for i in range(ind,length) :
        ds.append(arr[i])
        allsubSequence(arr,length,i+1,ds,result)
        ds.pop()

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds = []
        result = []
        n = len(nums)
        allsubSequence(nums,n,0,ds,result)

        return result
        
