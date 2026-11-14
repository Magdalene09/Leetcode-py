# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        if not root : return None

        if root.val == key :
            return self.attachRight(root)

        cur = root
        while cur :

            if cur.val > key :
                if cur.left and cur.left.val == key :
                    cur.left = self.attachRight(cur.left)
                    break

                else :
                    cur = cur.left

            else :
                if cur.right and cur.right.val == key :
                    cur.right = self.attachRight(cur.right)
                    break

                else :
                    cur = cur.right

        return root

    def attachRight(self, node) :

        if not node.left : return node.right
        if not node.right : return node.left

        leftChild = node.left
        node.left = None

        last_node = self.leftFind(node.right)
        last_node.left = leftChild

        return node.right

    def leftFind(self, node) :

        cur = node
        while cur.left :
            cur = cur.left

        return cur
