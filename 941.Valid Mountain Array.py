class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)
        if n < 3 : return False
        i = 1

        while i < n - 1 :

            if arr[i - 1] < arr[i] > arr[i + 1] :

                left = i
                right = i

                while left > 0 and arr[left - 1] < arr[left] : left -= 1
                while right < n - 1 and arr[right + 1] < arr[right] : right += 1

                return (right - left + 1) == n

            i += 1

        return False
