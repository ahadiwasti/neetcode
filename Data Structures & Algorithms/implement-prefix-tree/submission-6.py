class PrefixTree:
    def __init__(self):
        self.child = {}
        self.end = False

    def insert(self,word):
        for w in word:
            if w not in self.child:
                self.child[w] = PrefixTree()
            self = self.child[w]
        self.end = True

    def search(self,word):
        for w in word:
            if w not in self.child:
                return False
            self = self.child[w]
        return self.end

    def startsWith(self,word):
        for w in word:
            if w not in self.child:
                return False

            self = self.child[w]
        return True