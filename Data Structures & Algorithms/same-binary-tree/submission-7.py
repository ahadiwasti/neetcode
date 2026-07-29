# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode] ) -> TreeNode:
        if not p and not q:
            return True

        dq= deque()
        dq.append([p,q])

        while dq:
            nodep, nodeq = dq.popleft()

            if not nodep and not nodeq:
                continue

            if not nodep or not nodeq or nodep.val != nodeq.val:
                return False


            dq.append([nodep.left, nodeq.left])
            dq.append([nodep.right,nodeq.right])
        return True