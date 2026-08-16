def buildExpression(num, target, string, res, result, idx, length, prev) :

    if idx == length :
        if res == target : result.append(string)
        return

    for i in range(idx, length) :

        if i > idx and num[idx] == '0' : break

        curSt = num[idx : i + 1]
        curNum = int(num[idx : i + 1])

        if idx == 0 :
            buildExpression(num, target, curSt, res + curNum, result, i + 1, length, curNum)
        
        else :
            
            buildExpression(num, target, string + '*' + curSt, res - prev + (prev * curNum), result, i + 1, length, prev * curNum)
            buildExpression(num, target, string + '+' + curSt, res + curNum, result, i + 1, length, curNum)
            buildExpression(num, target, string + '-' + curSt, res - curNum, result, i + 1, length, -curNum)
            
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        n = len(num)

        string = ''
        result = []

        buildExpression(num, target, string, 0, result, 0, n, 1)
        return result
        
