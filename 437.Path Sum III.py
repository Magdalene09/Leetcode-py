# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def countPaths(node, target, prefixSum, count, hmap) :
    if not node : return

    prefixSum += node.val

    if prefixSum - target in hmap :
        count[0] += hmap[prefixSum - target]

    hmap[prefixSum] = hmap.get(prefixSum, 0) + 1

    countPaths(node.left, target, prefixSum, count, hmap)
    countPaths(node.right, target, prefixSum, count, hmap)

    hmap[prefixSum] -= 1

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        if not root : return 0
        hmap = {0 : 1}
        count = [0]

        countPaths(root, targetSum, 0, count, hmap)
        return count[0]
