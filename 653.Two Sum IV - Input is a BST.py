# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        lStack = []
        rStack = []

        self.leftIterator(root, lStack)
        self.rightIterator(root, rStack)  

        while lStack and rStack :
            low = lStack[-1]
            high = rStack[-1]

            if low.val >= high.val :
                break
        
            else :
                if low.val + high.val == k : return True

                elif low.val + high.val < k :
                    lStack.pop()
                    self.leftIterator(low.right, lStack)

                else :
                    rStack.pop()
                    self.rightIterator(high.left, rStack)

        return False

    def leftIterator(self, node, lStack) :

        cur = node
        while cur :
            lStack.append(cur)

            cur = cur.left

    def rightIterator(self, node, rStack) :

        cur = node
        while cur :
            rStack.append(cur)

            cur = cur.right
