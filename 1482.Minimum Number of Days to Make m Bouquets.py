def validBouquets(arr,day,m,k) :
    bloomed = 0
    count = 0
    for i in range(len(arr)) :
        if arr[i] <= day :
            count += 1

        else :
            bloomed += count // k
            count = 0
    bloomed += count // k

    if bloomed >= m :
        return True

    return False
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k :
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = high

        while low <= high :
            mid = (low + high) // 2

            bouquets = validBouquets(bloomDay,mid,m,k)

            if bouquets :
                ans = mid
                high = mid - 1

            else :
                low = mid + 1

        return ans


        
