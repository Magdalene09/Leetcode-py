# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def lvlOrdTrav(node) :

    dq = deque()
    dq.append(node)

    result = []

    while dq :
        size = len(dq)
        avg = 0

        for i in range(size) :
            tN = dq.popleft()
            avg += tN.val

            if tN.left : dq.append(tN.left)
            if tN.right : dq.append(tN.right)

        result.append(avg / size)
    
    return result


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:

        if not root : return []
        return lvlOrdTrav(root)
