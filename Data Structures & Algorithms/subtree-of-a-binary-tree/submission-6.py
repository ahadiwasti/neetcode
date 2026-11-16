# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(node, sub):
            if not node and not sub:
                return True

            if node and sub and node.val == sub.val:
                return sameTree(node.left,sub.left) and sameTree(node.right,sub.right)

        if not subRoot:
            return True

        if not root:
            return False

        if sameTree(root,subRoot):
            return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

    

            
