# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def build(preOrder, pStart, pEnd, inOrder, inStart, inEnd, iMap) :

    if pStart > pEnd or inStart > inEnd : return None

    node = TreeNode(preOrder[pStart])
    pI = iMap[preOrder[pStart]]
    dist = pI - inStart

    lNode = build(preOrder, pStart + 1, pStart + dist, inOrder, inStart, pI - 1, iMap)
    rNode = build(preOrder, pStart + dist + 1, pEnd, inOrder, pI + 1, inEnd, iMap)

    node.left = lNode
    node.right = rNode

    return node

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        n = len(preorder)

        iMap = {}

        for i in range(n) :
            iMap[inorder[i]] = i

        return build(preorder, 0, n - 1, inorder, 0, n - 1, iMap)
