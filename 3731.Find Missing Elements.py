class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        result = []
        a = set(nums)

        for num in range(mini + 1,maxi):
            if num not in a :
                result.append(num)


        return result
