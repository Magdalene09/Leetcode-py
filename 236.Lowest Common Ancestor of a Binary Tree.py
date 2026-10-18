# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def LCA(node, p, q) :

    if not node : return None

    if node is p or node is q :
        return node

    left = LCA(node.left, p, q)
    right = LCA(node.right, p, q)

    if left and right : return node

    return left or right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return LCA(root, p, q)
