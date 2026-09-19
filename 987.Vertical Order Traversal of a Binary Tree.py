# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def traversal(node, row, col, hmap) :

    if col not in hmap :
        hmap[col] = []

    hmap[col].append([row, node.val])

    if node.left : traversal(node.left, row + 1, col - 1, hmap)
    if node.right : traversal(node.right, row + 1, col + 1, hmap)

class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:

        if not root : return []

        hmap = {}
        result = []
        traversal(root, 0, 0, hmap)

        for key in sorted(hmap) :
            temp = []
            hmap[key].sort()

            for num in hmap[key] :
                temp.append(num[1])

            result.append(temp)

        return result
