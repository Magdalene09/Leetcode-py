# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:


        first = [root.val]
        second = [float("inf")]

        self.morrisTrav(root, first, second)
        return -1 if second[0] == float("inf") else second[0]

    def morrisTrav(self, node, first, second) :

        cur = node

        while cur :
            if not cur.left :
                if first[0] < cur.val < second[0] :
                    second[0] = cur.val
                
                cur = cur.right

            else :
                prev = cur.left
                while prev.right and prev.right != cur :
                    prev = prev.right


                if not prev.right :
                    prev.right = cur
                    if first[0] < cur.val < second[0] :
                        second[0] = cur.val

                    cur = cur.left

                else :
                    prev.right = None
                    cur = cur.right
