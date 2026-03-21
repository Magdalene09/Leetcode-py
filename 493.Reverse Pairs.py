def merge(arr,low,mid,high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high :
        if arr[left] < arr[right] :
            temp.append(arr[left])
            left += 1

        else :
            temp.append(arr[right])
            right += 1

    while left <= mid :
        temp.append(arr[left])
        left += 1

    while right <= high :
        temp.append(arr[right])
        right += 1

    for i in range(low,high + 1):
        arr[i] = temp[i-low]

def countP(arr,low,mid,high):
    count = 0
    right = mid + 1
    for i in range(low,mid+1):
        while right <= high and arr[i] > arr[right] * 2 :
            right += 1
        count += right - (mid + 1)

    return count


def ms(arr,low,high) :
    count = 0
    if low >= high :
        return 0
    
    mid = (low + high) // 2
    count += ms(arr,low,mid)
    count += ms(arr,mid+1,high)
    count += countP(arr,low,mid,high)
    merge(arr,low,mid,high)

    return count

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return ms(nums,0,len(nums)-1)
        
        
