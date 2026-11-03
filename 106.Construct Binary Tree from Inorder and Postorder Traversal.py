# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def build(inorder, postorder, iStart, iEnd, pStart, pEnd, iMap) :

    if iStart > iEnd or pStart > pEnd : return None

    node = TreeNode(postorder[pEnd])
    pI = iMap[postorder[pEnd]]
    dist = pI - iStart

    lNode = build(inorder, postorder, iStart, pI - 1, pStart, pStart + dist - 1, iMap)
    rNode = build(inorder, postorder, pI + 1, iEnd, pStart + dist, pEnd - 1, iMap)

    node.left = lNode
    node.right = rNode

    return node

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:

        n = len(inorder)
        iMap = {}

        for i in range(n) :
            iMap[inorder[i]] = i

        return build(inorder, postorder, 0, n - 1, 0, n - 1, iMap)
