# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return None
        d={}
        def bfs(start,end):
            if start>end:
                return [None]
            if (start,end) in d:
                return d[(start,end)]
            tree=[]
            for rootval in range(start,end+1):
                lt=bfs(start,rootval-1)
                rt=bfs(rootval+1,end)

                for i in lt:
                    for j in rt:
                        node=TreeNode(rootval)
                        node.left=i
                        node.right=j

                        tree.append(node)
            d[start,end]=tree
            return tree
        return bfs(1,n)
