# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

def view(node, result) :
    dq = deque()
    dq.append(node)

    while dq :
        size = len(dq)

        for i in range(size) :
            treeNode = dq.popleft()

            if i == size - 1 :
                result.append(treeNode.val)

            if treeNode.left : dq.append(treeNode.left)
            if treeNode.right : dq.append(treeNode.right)

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if not root : return []

        result = []
        view(root, result)
        return result
