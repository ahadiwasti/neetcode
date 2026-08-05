class TreeNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self,word:str):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TreeNode()
            curr = curr.children[char]

        curr.endofword = True

    
    def search(self,word)->bool:
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                
                else:
                    if c not in curr.children:
                        return False
                    curr=curr.children[c]
            return curr.endofword

        return dfs(0,self.root)