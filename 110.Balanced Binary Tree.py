# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeDepth(node) :

    if not node : return 0

    left = treeDepth(node.left)
    if left == -1 : return -1

    right = treeDepth(node.right)
    if right == -1 : return -1

    if abs(left - right) > 1 : return -1
    return 1 + max(left, right)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ans = treeDepth(root)

        if ans == -1 : return False
        else : return True
