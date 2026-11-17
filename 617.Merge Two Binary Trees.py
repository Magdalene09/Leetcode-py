# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        return self.merge(root1, root2)

    def merge(self, n1, n2) :

        if not n1 :
            return n2

        if not n2 :
            return n1

        n2.val += n1.val
        n2.left = self.merge(n1.left, n2.left)
        n2.right = self.merge(n1.right, n2.right)

        return n2
