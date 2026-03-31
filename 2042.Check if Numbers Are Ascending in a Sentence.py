class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        i = 0
        n = len(s)
        prev = -1

        while i < n :
            if s[i].isdigit() :
                num = 0
                while i < n and s[i].isdigit() :
                    num = num * 10 + (ord(s[i])-ord('0'))
                    i += 1

                if num <= prev :
                    return False
                
                prev = num

            else :
                i += 1

        return True

         


        
