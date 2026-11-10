# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def mTs(node) :
    cur = node

    while cur :
        if not cur.left :
            ans = cur.val
            cur = cur.right

            break

        else :
            prev = cur.left

            while prev.right and prev.right != cur :
                prev = prev.right

            if not prev.right :
                prev.right = cur
                cur = cur.left

            else :
                ans = prev.right.val
                prev.right = None
                cur = cur.right

                break
    
    return ans, cur

class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.ptr = root

    def next(self) -> int:
        ans, self.ptr = mTs(self.ptr)
        return ans
        

    def hasNext(self) -> bool:
        return True if self.ptr else False
