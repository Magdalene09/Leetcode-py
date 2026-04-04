class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r :
            mid = (l + r) // 2

            if nums[mid] == target :
                return True
            
            if nums[mid] == nums[r] == nums[l] :
                l += 1
                r -= 1
                continue

            if nums[mid] >= nums[l] :
                if nums[mid] > target and nums[l] <= target :
                    r = mid - 1
                
                else :
                    l = mid + 1

            else :
                if nums[mid] < target and nums[r] >= target :
                    l = mid + 1

                else :
                    r = mid - 1

        return False

            
