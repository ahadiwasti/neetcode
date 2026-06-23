# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
       if not preorder or not inorder:
        return None
       bst = TreeNode(preorder[0])
       indexof = inorder.index(preorder[0])
       leftpre,rightpre = preorder[1:indexof+1],preorder[indexof+1:]
       leftin,rightin = inorder[:indexof],inorder[indexof+1:]
       bst.left = self.buildTree(leftpre,leftin)
       bst.right = self.buildTree(rightpre,rightin)
       return bst