# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfsMaxSum(node, maxSum) :
    
    if not node : return 0

    leftSum = max(0, dfsMaxSum(node.left, maxSum))
    rightSum = max(0, dfsMaxSum(node.right, maxSum))

    maxSum[0] = max(maxSum[0], leftSum + rightSum + node.val)

    return node.val + max(leftSum, rightSum)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum = [float("-inf")]
        dfsMaxSum(root, maxSum)

        return maxSum[0]
