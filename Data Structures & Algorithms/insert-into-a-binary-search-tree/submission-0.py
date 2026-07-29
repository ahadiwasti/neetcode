# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val=val,right=None,left=None)

        curr = root
        while curr:
            if curr.val > val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left=TreeNode(val=val,right=None,left=None)
                    break
            else:
                if curr.right:
                    curr= curr.right
                else:
                    curr.right=TreeNode(val=val,right=None,left=None)
                    break

        return root