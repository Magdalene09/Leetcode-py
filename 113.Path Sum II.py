# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def allSumPaths(node, path, paths, target, endSum) :

    if not node : return

    if not node.left and not node.right :
        if endSum + node.val == target :
            path.append(node.val)
            paths.append(path[:])
            path.pop()

        return

    path.append(node.val)
    allSumPaths(node.left, path, paths, target, endSum + node.val)
    allSumPaths(node.right, path, paths, target, endSum + node.val)
    path.pop()

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:

        if not root : return []

        paths = []
        path = []

        allSumPaths(root, path, paths, targetSum, 0)
        return paths
