class WordDictionary:
    def __init__(self):
        self.child = {}
        self.endofword = False

    def addWord(self,word):
        for w in word:
            if w not in self.child:
                self.child[w] = WordDictionary()
            self = self.child[w]
        self.endofword = True

    def search(self,word)->bool:
        def dfs(j,root):
            for i in range(j,len(word)):
                char = word[i]
                if char == ".":
                    for child in root.child.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if char not in root.child:
                        return False
                    root = root.child[char]
            return root.endofword

        return dfs(0,self)