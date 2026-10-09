# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfsLeft(node) :
    cur = node
    height = 0

    while cur :
        height += 1

        cur = cur.left

    return height

def dfsRight(node) :
    cur = node
    height = 0

    while cur :
        height += 1

        cur = cur.right

    return height

class Solution:
    def countNodes(self, root: TreeNode | None) -> int:

        if not root : return 0

        leftHeight = dfsLeft(root)
        rightHeight = dfsRight(root)

        if leftHeight == rightHeight : return (1 << leftHeight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
