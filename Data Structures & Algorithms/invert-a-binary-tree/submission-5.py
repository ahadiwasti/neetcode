class Solution:
    def invertTree(self, root:Optional[TreeNode])-> Optionalp[TreeNode]:
        if not root:
            return None
        # tmp = root.left
        root.left , root.right = root.right, root.left
        # root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root