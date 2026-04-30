class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []

        for i in range(n) :
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1

            stack.append(num[i])

        # edge case 1 : if the elements in the num are already in the lowest order must remove k elements to make it small
        while k > 0 :
            stack.pop()
            k -= 1

        # edge case 2 : after this pop it is possible that if k == n then everything is popped
        if not stack : return "0"

        string = ""
        while stack : 
            string += stack.pop()

        # edge case 3 : if the given string has zeroes starting at the first must be removed form the string
        string = string.rstrip("0")
        string = string[::-1]

        # edge case 4 : after pop no elements in the string
        if not string : return "0"
        return string
