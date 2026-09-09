# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeDepth(node) :

    if not node : return 0

    left = treeDepth(node.left)
    right = treeDepth(node.right)

    return 1 + max(left, right)

def depthDiscovery(node, maxDist) :

    if not node : return

    ld = treeDepth(node.left) 
    rd = treeDepth(node.right)

    maxDist = max(ld + rd, maxDist)

    depthDiscovery(node.left, maxDist)
    depthDiscovery(node.right, maxDist)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDist = 0
        depthDiscovery(root, maxDist)

        return maxDist
