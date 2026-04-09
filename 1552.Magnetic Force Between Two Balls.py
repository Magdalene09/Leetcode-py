def maxForce(arr,distance,m) :
    noOffBalls = 1
    lastPosn = arr[0]

    for i in range(1,len(arr)) :
        if arr[i] - lastPosn >= distance :
            noOffBalls += 1
            lastPosn = arr[i]
        
        if noOffBalls >= m :
            return True

    return False

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        low = 1
        high = position[n-1] - position[0]
        ans = 1

        while low <= high :
            mid = ( low + high ) // 2

            validPosn = maxForce(position,mid,m)

            if validPosn :
                ans = mid
                low = mid + 1
            
            else :
                high = mid - 1

        return ans


        
