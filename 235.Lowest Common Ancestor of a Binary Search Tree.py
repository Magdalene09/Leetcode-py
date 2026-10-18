# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def LCA(node, p ,q) :
    if not node : return None

    if p.val < node.val and q.val < node.val :
        return LCA(node.left, p ,q)

    if p.val > node.val and q.val > node.val :
        return LCA(node.right, p, q)

    return node

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        return LCA(root, p, q)
