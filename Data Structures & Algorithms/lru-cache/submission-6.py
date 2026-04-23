# solution 1 doubly linked list
class Node:
    def __init__(self,key,val):
        self.key, self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        curNode = self.cache[key]
        preNode = curNode.prev
        nxtNode = curNode.next
        self.remove(curNode)
        self.insert_to_tail(curNode)
        return curNode.val
    
    def insert_to_tail(self, node: Node) -> None:
        prevNode = self.tail.prev
        prevNode.next = node
        node.next = self.tail
        node.prev = prevNode
        self.tail.prev = node
        self.cache[node.key] = node
    
    def remove(self,node:Node) -> None:
        prevNode = node.prev
        nxtNode = node.next
        prevNode.next = nxtNode
        nxtNode.prev = prevNode
        del self.cache[node.key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])      
        curNode = Node(key,value)
        self.insert_to_tail(curNode)
        if len(self.cache) > self.capacity:
            self.remove(self.head.next)
