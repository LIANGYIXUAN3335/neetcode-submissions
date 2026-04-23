class Node:
    def __init__(self,key :int, val : int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self,node:Node)->None:
        preNode = node.prev
        nextNode = node.next
        preNode.next = nextNode
        nextNode.prev = preNode
        del self.cache[node.key]

    def insert(self,node:Node)->None:
        preNode = self.tail.prev
        preNode.next = node
        node.next = self.tail
        node.prev = preNode
        self.tail.prev = node
        self.cache[node.key] = node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curNode = self.cache[key]
        self.remove(curNode)
        self.insert(curNode)
        return curNode.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        curNode = Node(key,value)
        self.insert(curNode)
        if len(self.cache) > self.cap:
            self.remove(self.head.next)
        
