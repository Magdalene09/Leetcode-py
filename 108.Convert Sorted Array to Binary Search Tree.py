# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def treeBuilder(nums, low, high) :
    if low > high :
        return None

    mid = (low + high) // 2
    root = TreeNode(nums[mid])

    root.left = treeBuilder(nums, low, mid - 1)
    root.right = treeBuilder(nums,mid + 1, high)

    return root

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        return treeBuilder(nums, 0, len(nums) - 1)
