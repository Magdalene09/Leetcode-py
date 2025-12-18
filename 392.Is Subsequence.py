class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        for right in range(len(t)):
            if len(s) > left and t[right] == s[left]:
                left += 1

        return left == len(s)


        
