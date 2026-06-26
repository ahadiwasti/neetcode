# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def preorder(root):
            if not root:
                return "N"
            lefts =  preorder(root.left)
            rights =  preorder(root.right)
            return ",".join([str(root.val),lefts,rights])

        return preorder(root)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = collections.deque(data.split(","))
        def dfs():
            val = values.popleft()
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
