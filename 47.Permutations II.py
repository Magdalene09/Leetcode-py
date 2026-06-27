def findPermutation(arr, length, result, index):

    if index == length:
        result.append(arr[:])
        return

    seen = set()

    for i in range(index, length):

        if arr[i] in seen:
            continue

        seen.add(arr[i])
        arr[index], arr[i] = arr[i], arr[index]
        findPermutation(arr, length, result, index + 1)
        arr[index], arr[i] = arr[i], arr[index]


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result = []
        findPermutation(nums, n, result, 0)

        return result
