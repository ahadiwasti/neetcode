# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        dq=deque()
        res=[]
        def dfs(root):
            if root:
                
                root.left = dfs(root.left)
                res.append(root.val)
                root.right= dfs(root.right)
               

            return res
        print(res)
        return dfs(root)