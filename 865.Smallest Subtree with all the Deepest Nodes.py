# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def LCA(node) :

    if not node : return None, 0

    lNode, lHeight = LCA(node.left)
    rNode, rHeight = LCA(node.right)

    if lHeight == rHeight :
        return node, lHeight + 1

    if lHeight > rHeight :
        return lNode, lHeight + 1

    return rNode, rHeight + 1

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode | None) -> TreeNode | None:

        ansNode, height = LCA(root)
        return ansNode
