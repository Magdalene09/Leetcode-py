def nxtSmallerElement(arr):
    n = len(arr)
    result = [0] * n
    stack = []

    for i in range(n-1,-1,-1) :
        while stack and arr[stack[-1]] >= arr[i] :
            stack.pop()

        result[i] = n if not stack else stack[-1]
        stack.append(i)

    return result

def prevSmallerElement(arr):
    n = len(arr)
    result = [0] * n
    stack = []

    for i in range(n) :
        while stack and arr[stack[-1]] > arr[i] :
            stack.pop()

        result[i] = -1 if not stack else stack[-1]
        stack.append(i)

    return result

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = int(1e9 + 7)
        n = len(arr)
        prevSmall = prevSmallerElement(arr)
        nextSmall = nxtSmallerElement(arr)
        total = 0

        for i in range(n) :
            leftContribution = i - prevSmall[i]
            rightContribution = nextSmall[i] - i

            total = (total + (leftContribution * rightContribution * arr[i]) % MOD ) % MOD

        return total
    

        
