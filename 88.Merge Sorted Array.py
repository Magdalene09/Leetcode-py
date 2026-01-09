class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:


        i = m - 1
        j = n - 1
        np = n + m - 1

        while i >= 0 and j >= 0 :
            if nums1[i] < nums2[j] :
                nums1[np] = nums2[j]
                j -= 1
                np -= 1

            else:
                nums1[np] = nums1[i]
                i -= 1
                np -= 1

        while j >= 0 :
            nums1[np] = nums2[j]
            np -= 1
            j -=1

        
          


        
