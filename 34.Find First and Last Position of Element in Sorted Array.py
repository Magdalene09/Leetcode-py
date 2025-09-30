class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def ff(nums,target):
            left=0
            right=len(nums)-1
            ans=-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
                    
            return ans
        
        def fl(nums,target):
            left=0
            right=len(nums)-1
            ans=-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1    
                else:
                    right = mid -1
            
            return ans
        
        return [ff(nums,target),fl(nums,target)]
        
        
        
