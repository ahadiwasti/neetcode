# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left = min(p.val,q.val)
        right = max(p.val,q.val)

        if left <= root.val <= right:
            return root

        if root.val < left and root.val < right:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)
