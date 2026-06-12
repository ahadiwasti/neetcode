# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not q:
            return True
        if not p and q:
            return False
        if self.isSameTree(p,q):
            return True
        return (self.isSubtree(p.left,q) or self.isSubtree(p.right,q))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        return False