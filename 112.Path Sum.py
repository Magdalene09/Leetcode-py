# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def pathSum(node, target, endSum) :

    if not node : return False

    if not node.left and not node.right :
        if endSum + node.val == target : 
            return True

        return False

    return pathSum(node.left, target, node.val + endSum) or pathSum(node.right, target, node.val + endSum)
    
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        if not root : return False
        return pathSum(root, targetSum, 0)
