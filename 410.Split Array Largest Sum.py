def calcSum(arr,cap,sub) :
    subCnt = 1
    _sum = 0

    for i in range(len(arr)) :
        if _sum + arr[i] > cap :
            subCnt += 1
            _sum = arr[i]

        else :
            _sum += arr[i]

        if subCnt > sub :
            return False

    return True
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = sum(nums)

        while low <= high :
            mid = ( low + high ) // 2

            subSum = calcSum(nums,mid,k)

            if subSum :
                ans = mid
                high = mid - 1

            else :
                low = mid + 1

        return ans

        
