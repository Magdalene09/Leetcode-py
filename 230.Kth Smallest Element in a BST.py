# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        count = 0
        kth_element = -1

        cur = root
        while cur :
            if not cur.left :
                if kth_element == -1 :
                    count += 1
                    if count == k : kth_element = cur.val
                    
                cur = cur.right

            else :
                prev = cur.left
                while prev.right and prev.right != cur :
                    prev = prev.right

                if not prev.right :
                    prev.right = cur
                    cur = cur.left

                else :
                    prev.right = None
                    if kth_element == -1 :
                        count += 1
                        if count == k : kth_element = cur.val

                    cur = cur.right

        return kth_element
