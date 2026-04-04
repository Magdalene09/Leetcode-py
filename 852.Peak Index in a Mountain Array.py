class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        low = 1
        high = n - 2

        while low <= high :
            mid = ( low + high ) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1] :
                return mid

            elif arr[mid] > arr[mid - 1] :
                low = mid + 1

            else :
                high = mid - 1

        return -1 
        
