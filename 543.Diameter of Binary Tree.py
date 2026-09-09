# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeDepth(node, diameter) :

    if not node : return 0

    left = treeDepth(node.left, diameter)
    right = treeDepth(node.right, diameter)

    diameter[0] = max(diameter[0], left + right)

    return 1 + max(left, right)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]
        treeDepth(root, diameter)

        return diameter[0]
