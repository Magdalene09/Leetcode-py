class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = [0] * len(nums) 

        for i in range(2 * len(nums)-1, -1, -1) :
            idx = i % len(nums)
            while stack and stack[-1] <= nums[idx] :
                stack.pop()

            if i < len(nums) :
                if not stack :
                    result[idx] = -1

                else :
                    result[idx] = stack[-1]

            stack.append(nums[idx])

        return result



            

