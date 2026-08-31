def maxSubsequence(arr, limit) :

    n = len(arr)
    remove = n - limit

    st = []

    for i in range(n) :

        while st and remove > 0 and st[-1] < arr[i] :
            st.pop()
            remove -= 1

        st.append(arr[i])

    return st[:limit]

def merge(stn1, stn2) :

    ans = []

    n = len(stn1)
    m = len(stn2)

    i = 0
    j = 0

    while i < n and j < m :

        if stn1[i] > stn2[j] :
            ans.append(stn1[i])
            i += 1

        elif stn2[j] > stn1[i] :
            ans.append(stn2[j])
            j += 1

        else :
            x = i
            y = j

            while x < n and y < m and stn1[x] == stn2[y] :
                x += 1
                y += 1

            if x == n :
                ans.append(stn2[j])
                j += 1

            elif y == m :
                ans.append(stn1[i])
                i += 1

            elif stn1[x] > stn2[y] :
                ans.append(stn1[i])
                i += 1

            else :
                ans.append(stn2[j])
                j += 1

    while i < n : 
        ans.append(stn1[i])
        i += 1

    while j < m :
        ans.append(stn2[j])
        j += 1

    return ans

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        result = []

        lb = max(0, k - len(nums2))
        ub = min(len(nums1), k)

        for take1 in range(lb, ub + 1) :

            take2 = k - take1

            stn1 = maxSubsequence(nums1, take1)
            stn2 = maxSubsequence(nums2, take2)

            final = merge(stn1, stn2)
            result = max(result, final)

        return result
