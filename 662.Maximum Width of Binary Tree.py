# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def endNodes(node, indexArr, level, index, maxWidth) :

    if not node : return

    if len(indexArr) == level :
        indexArr.append(index)

    maxWidth[0] = max(maxWidth[0], index - indexArr[level] + 1)

    endNodes(node.left, indexArr, level + 1, 2 * index, maxWidth)
    endNodes(node.right, indexArr, level + 1, (2 * index) + 1, maxWidth)

class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:

        if not root : return 0

        indexArr = []
        maxWidth = [0]

        endNodes(root, indexArr, 0, 0, maxWidth)
        return maxWidth[0]
