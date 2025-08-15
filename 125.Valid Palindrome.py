class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s.lower():
            if not i.isalnum():
                s.remove(i)
        return s==s[::-1]

       
