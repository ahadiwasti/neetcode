class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

    def addWord(self,word):
        root = self

        for w in word:
            if w not in root.children:
                root.children[w] = TrieNode()
            root = root.children[w]

        root.endofword = True

class Solution:
    def findWords(self,board,words)->list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows,cols = len(board),len(board[0])
        visited, res = set(),set()
        def dfs(r,c,node,word):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or board[r][c] not in node.children:
                return 

            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.endofword:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))


        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(res)




