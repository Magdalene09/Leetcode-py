class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        smaller = []
        equal = []
        greater = []

        for i in range(n) :
            if nums[i] < pivot :
                smaller.append(nums[i])

            elif nums[i] == pivot :
                equal.append(nums[i])

            else :
                greater.append(nums[i])

        return smaller + equal + greater
