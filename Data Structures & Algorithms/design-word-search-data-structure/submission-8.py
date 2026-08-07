class TreeNode:
    def __init__(self):
        self.child = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self,word):
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TreeNode()
            curr = curr.child[w]

        curr.end = True

    # def search(self,word):
    #     curr = self.root
    #     for w in word:
    #         if w not in curr.child:
    #             return False
    #         curr = curr.child[w]
    #     return curr.end

    def search(self,word):
        curr = self.root
        def dfs(j,node):
            for i in range(j,len(word)):
                char = word[i]
                if char == ".":
                    for child in node.child.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if char not in node.child:
                        return False
                    node = node.child[char]
            return node.end


        return dfs(0,curr)
