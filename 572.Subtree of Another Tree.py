# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def srCheck(node, srNode) :

    if not node and not srNode : return True
    if not node or not srNode : return False
    if node.val != srNode.val : return False
    
    if not srCheck(node.left, srNode.left) : return False
    if not srCheck(node.right, srNode.right) : return False

    return True
 
def dfs(node, srNode) :

    if not node : return False

    if node.val == srNode.val :
        if srCheck(node, srNode) : return True

    if dfs(node.left, srNode) : return True
    if dfs(node.right, srNode) : return True

    return False

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if not subRoot : return True
        return dfs(root, subRoot)
