class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1

        arr = [0] * len(nums)
        np = len(arr) - 1 

        while l <= r :
            if abs(nums[l]) > abs(nums[r]) :
                arr[np] = nums[l] * nums[l]
                l += 1


            
            else :
                arr[np] = nums[r] * nums[r]
                r -= 1
            
            np -= 1

        return arr

            
        
