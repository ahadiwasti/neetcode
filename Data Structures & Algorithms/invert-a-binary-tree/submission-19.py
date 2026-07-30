class Solution:
    def invertTree(self, root:Optional[TreeNode])-> Optionalp[TreeNode]:
        dq=deque()

        dq.append(root)

        while dq:
            node = dq.popleft()
            if node:
                node.left , node.right = node.right , node.left
                dq.append(node.left)
                dq.append(node.right)

        return root
