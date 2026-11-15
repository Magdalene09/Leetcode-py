# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        self.morrisTrav(root)


    def morrisTrav(self, node) :

        if not node : return

        cur = node

        first_node = None
        second_node = None
        prev_node = None

        while cur :
            if not cur.left :

                if prev_node :
                    if prev_node.val > cur.val :
                        if not first_node :
                            first_node = prev_node
                        
                        second_node = cur

                prev_node = cur
                cur = cur.right

            else :
                prev = cur.left

                while prev.right and prev.right != cur :
                    prev = prev.right

                if not prev.right :
                    prev.right = cur
                    cur = cur.left

                else :

                    if prev_node.val > cur.val :
                        if not first_node :
                            first_node = prev_node

                        second_node = cur

                    prev_node = cur
                    prev.right = None
                    cur = cur.right

        first_node.val, second_node.val = second_node.val, first_node.val
