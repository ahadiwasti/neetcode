# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(root):
            if root:
                
                root.left = dfs(root.left)
                
                root.right= dfs(root.right)
                res.append(root.val)

            return res
        print(res)
        return dfs(root)