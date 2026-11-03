# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def build(preorder, postorder, pStart, pEnd, poStart, poEnd, iMap) :

    if pStart > pEnd or poStart > poEnd : return None

    node = TreeNode(preorder[pStart])
    if pStart == pEnd or poStart == poEnd : return node

    lnext = preorder[pStart + 1]

    pI = iMap[lnext]
    size = pI - poStart
    
    node.left = build(preorder, postorder, pStart + 1, pStart + size + 1, poStart, pI, iMap)
    node.right = build(preorder, postorder, pStart + size + 2, pEnd, pI + 1, poEnd - 1, iMap)

    return node

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:

        n = len(postorder)
        iMap = {}

        for i in range(n) :
            iMap[postorder[i]] = i

        return build(preorder, postorder, 0, n - 1, 0, n - 1, iMap)
