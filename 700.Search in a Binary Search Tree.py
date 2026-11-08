# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def findNode(node, val) :
    
    cur = node

    while cur and cur.val != val :

        if cur.val > val :
            cur = cur.left

        elif cur.val < val :
            cur = cur.right

    return cur

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        return findNode(root, val)
