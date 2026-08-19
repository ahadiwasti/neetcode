class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.right = Node()
        self.left = Node()
        self.left.next = self.right
        self.right.prev = self.left

    def rem(self,node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self,node):
        prev,next = self.right.prev, self.right
        prev.next= next.prev = node
        node.prev, node.next = prev,next


    def put(self, key,value):
        if key in self.cache:
            self.rem(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        while len(self.cache)>self.capacity:
            lru = self.left.next
            self.rem(lru)
            del self.cache[lru.key]

    
    def get(self,key):
        if key in self.cache:
            self.rem(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
