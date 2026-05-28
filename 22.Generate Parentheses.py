def validParenthesis(string,start,end,length,result) :
    if start == length and end == length :
        result.append(string)
        return
    
    if start < length : validParenthesis(string + '(',start + 1,end,length,result)
    if end < start: validParenthesis(string + ')',start,end + 1,length,result)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        string = ''
        validParenthesis(string,0,0,n,result)
        return result
