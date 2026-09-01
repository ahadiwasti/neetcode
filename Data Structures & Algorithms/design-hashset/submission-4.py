class ListNode:
    def __init__(self, key = -1):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.capacity = 1000
        self.set = [ListNode() for _ in range(self.capacity)]

    def hash(self,key):
        return key%self.capacity

    def add(self, key):
        curr = self.set[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                return 
            curr = curr.next
        curr.next = ListNode(key)

    def contains(self, key):
        curr = self.set[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

    def remove(self, key):
        curr = self.set[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# T:O(n/k)
# S:O(k+m)
