# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        
        cur = root

        while cur :
            
            if not cur.left : cur = cur.right

            else :

                prev = cur.left

                while prev.right :
                    prev = prev.right

                prev.right = cur.right
                cur.right = cur.left
                cur.left = None

                cur = cur.right
