class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Solution:
    def __init__(self):
        self.root = TreeNode()

    def add(self,word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TreeNode()
            curr = curr.child[w]
        curr.end = True
    
    def findWords(self,board,words):
        curr = self.root
        for w in words:
            self.add(w)

        rows,cols = len(board),len(board[0])
        visited,res = set(),set()

        def dfs(r,c,node,word):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] not in node.child:
                return 
            
            visited.add((r,c))
            node = node.child[board[r][c]]
            word += board[r][c]

            if node.end:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,curr,"")
        return list(res)


