class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        maxWidth = 0

        for i in range(n):
            while stack and heights[stack[-1]] > heights[i] :
                top = stack.pop()
                prevSmallEle = stack[-1] if stack else -1
                width = heights[top] * (i - prevSmallEle - 1)
                maxWidth = max(maxWidth,width)

            stack.append(i)

        # when stack still has elements denotes that those elements doesnt have nxtSmallEle

        while stack :
            top = stack.pop()
            prevSmallEle = stack[-1] if stack else -1
            width = heights[top] * (n - prevSmallEle - 1)
            maxWidth = max(maxWidth,width)

        return maxWidth
