def findPeak(arr,length) :
    low = 1
    high = length - 2

    while low <= high :
        mid = ( low + high ) // 2
        val = arr.get(mid)
        left = arr.get(mid - 1)
        right = arr.get(mid + 1)

        if left < val and right < val :
            return mid

        elif val < right :
            low = mid + 1

        else :
            high = mid - 1

    return -1

def bsAscending(arr,peak,target) :
    low = 0
    high = peak

    while low <= high :
        mid = ( low + high ) // 2
        val = arr.get(mid)

        if val == target :
            return mid

        elif val > target : 
            high = mid - 1

        else :
            low = mid + 1
        
    return -1

def bsDescending(arr,peak,length,target) :
    low = peak + 1
    high = length - 1

    while low <= high :
        mid = ( low + high ) // 2
        val = arr.get(mid)

        if val == target :
            return mid

        elif val > target :
            low = mid + 1

        else :
            high = mid - 1
    
    return -1
    
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peak = findPeak(mountainArr,n)
        bsAmid = bsAscending(mountainArr,peak,target)

        if bsAmid != -1 :
            return bsAmid
        return bsDescending(mountainArr,peak,n,target)

        

        

        
        
