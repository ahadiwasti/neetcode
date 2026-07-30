# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        def dfs(root,maxval):
            if not root:
                return
            if root.right:
                dfs(root.right,max(root.val,maxval))
            if root.left:
                dfs(root.left,max(root.val,maxval))

            if maxval <= root.val:
                res.append(maxval)

        dfs(root,float('-inf'))
        return len(res)