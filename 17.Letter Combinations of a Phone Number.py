def subsequences(digits,ind,string,result,hmap,length) :
    if ind >= length :
        result.append(string)
        return

    for char in hmap[digits[ind]] :
        subsequences(digits,ind + 1,string + char,result,hmap,length)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case :
        if not digits : return []
        hmap = {'2' : ['a','b','c'] , '3' : ['d','e','f'] , '4' : ['g','h','i'] ,'5' : ['j','k','l'] , '6' : ['m','n','o'] , '7' : ['p','q','r','s'] , '8' : ['t','u','v'], '9' : ['w','x','y','z']}

        result = []
        string = ''
        n = len(digits)
        subsequences(digits,0,string,result,hmap,n)
        return result
