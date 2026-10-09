# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

def parentFind(node, pMap, parent) :
    if not node : return 

    pMap[node] = parent
    parentFind(node.left, pMap, node)
    parentFind(node.right, pMap, node)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        result = []

        parentMap = {}
        parentFind(root, parentMap, None)

        visited = set()
        dq = deque()

        dq.append(target)
        visited.add(target)
        distance = 0

        while dq :
            size = len(dq)
            if distance == k : break

            for i in range(size) :
                tNode = dq.popleft()

                if tNode.left and tNode.left not in visited :
                    dq.append(tNode.left)
                    visited.add(tNode.left)

                if tNode.right and tNode.right not in visited :
                    dq.append(tNode.right)
                    visited.add(tNode.right)

                parent = parentMap[tNode]

                if parent and parent not in visited :
                    dq.append(parent)
                    visited.add(parent)

            distance += 1

        
        while dq :
            result.append(dq.popleft().val)

        return result
