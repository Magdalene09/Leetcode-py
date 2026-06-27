def findPermutation(arr, length, result, index) :

    if index == length :
        result.append(arr[:])
        return

    for i in range(index,length) :
        arr[index], arr[i] = arr[i], arr[index]
        findPermutation(arr, length, result, index+1)
        arr[index], arr[i] = arr[i], arr[index]
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []
        findPermutation(nums, n, result, 0)

        return result
