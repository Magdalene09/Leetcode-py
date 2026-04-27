def nxtSmallerElement(arr,length):
    result = [0] * length
    stack = []

    for i in range(length-1,-1,-1) :
        while stack and arr[stack[-1]] >= arr[i] :
            stack.pop()

        if not stack : result[i] = length
        else : result[i] = stack[-1]

        stack.append(i)

    return result

def prevSmallerElement(arr,length):
    result = [0] * length
    stack = []

    for i in range(length) :
        while stack and arr[stack[-1]] > arr[i] :
            stack.pop()

        if not stack : result[i] = -1
        else : result[i] = stack[-1]

        stack.append(i)

    return result

def nxtGreaterElement(arr,length):
    result = [0] * length
    stack = []

    for i in range(length-1,-1,-1) :
        while stack and arr[stack[-1]] <= arr[i] :
            stack.pop()

        if not stack : result[i] = length
        else : result[i] = stack[-1]

        stack.append(i)

    return result

def prevGreaterElement(arr,length):
    result = [0] * length
    stack = []

    for i in range(length) :
        while stack and arr[stack[-1]] < arr[i] :
            stack.pop()

        if not stack : result[i] = -1
        else : result[i] = stack[-1]

        stack.append(i)

    return result

def sumArrayMinimum(arr) :
    n = len(arr)
    total = 0

    nxtSmaller = nxtSmallerElement(arr,n)
    prevSmaller = prevSmallerElement(arr,n)

    for i in range(n) :
        leftContribution = i - prevSmaller[i]
        rightContribution = nxtSmaller[i] - i

        total = total + (leftContribution * rightContribution * arr[i])

    return total

def sumArrayMaximum(arr) :
    n = len(arr)
    total = 0

    nxtGreater = nxtGreaterElement(arr,n)
    prevGreater = prevGreaterElement(arr,n)

    for i in range(n) :
        leftContribution = i - prevGreater[i]
        rightContribution = nxtGreater[i] - i

        total = total + (leftContribution * rightContribution * arr[i])

    return total


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        return sumArrayMaximum(nums) - sumArrayMinimum(nums)
