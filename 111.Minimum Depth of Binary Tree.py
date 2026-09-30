# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(node) :

    if not node : return 0

    left = height(node.left)
    right = height(node.right)

    if left == 0 : return 1 + right
    elif right == 0 : return 1 + left

    return 1 + min(left, right)

class Solution:
    def minDepth(self, root: TreeNode | None) -> int:

        return height(root)
