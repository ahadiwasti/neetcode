# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(root,left,right):
            if left <= root.val <= right:
                return root

            if root.val < left and root.val < right:
                return dfs(root.right, left, right)
            else:
                return dfs(root.left,left,right)


        
        return dfs(root, min(p.val,q.val), max(p.val,q.val))