class ListNode:
    def __init__(self,key=-1,value=-1,next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.capacity = 1000
        self.size = 0
        self.map = [ListNode() for _ in range(self.capacity)]
    
    def hash(self,key:int)->int:
        return key%self.capacity
    
    def put(self,key,value)-> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)
        self.size +=1

        if self.size / self.capacity > 0.75:
            self._resize()


    def get(self,key)->int:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self,key):
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -=1
                return
            curr = curr.next
    
    def _resize(self):
        oldMap = self.map
        self.capacity *= 2
        self.map = [ListNode() for _ in range(self.capacity)]

        for curr in oldMap:
            while curr.next:
                newcurr = self.map[self.hash(curr.next.key)]
                while newcurr.next:
                    newcurr = newcurr.next
                newcurr.next = ListNode(curr.next.key,curr.next.value)
                curr = curr.next
    
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)