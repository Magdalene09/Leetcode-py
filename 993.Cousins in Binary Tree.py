# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:

        if not root : return False

        dq = deque()
        dq.append([root,0,-1])
        ans = []

        while dq :
            size = len(dq)

            for i in range(size) :
                node = dq.popleft()

                value = node[0].val
                lvl = node[1]
                childRoot = node[2]

                if value == x or value == y :
                    ans.append([lvl, childRoot])
                
                if len(ans) == 2 : 

                    if ans[0][0] == ans[1][0] and ans[0][1] != ans[1][1] : return True
                    return False
                
                if node[0].left : dq.append([node[0].left, lvl + 1, value])
                if node[0].right : dq.append([node[0].right, lvl + 1, value])

        return False
