# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rangeCheck(node, min_val, max_val) :

    if not node : return True
    if node.val <= min_val or node.val >= max_val : return False

    return rangeCheck(node.left, min_val, node.val) and rangeCheck(node.right, node.val, max_val)
    

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        return rangeCheck(root, float("-inf"), float("inf"))
