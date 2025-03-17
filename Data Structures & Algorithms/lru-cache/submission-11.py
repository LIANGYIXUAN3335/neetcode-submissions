class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        self.start = Node(-1,-1)
        self.end = Node(-2,-2)
        self.start.next = self.end
        self.end.pre = self.start

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.addLast(node)
        return self.cache[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.addLast(node)
        else:
            node = Node(key,value)
            self.addLast(node)
            self.size += 1
        self.cache[key] = node
        if self.size > self.capacity:
            lRUNode = self.start.next
            self.remove(lRUNode)
            self.size -= 1
            del self.cache[lRUNode.key]

    def addLast(self, node) -> None:
        preNode = self.end.pre
        node.pre = preNode
        node.next = self.end
        preNode.next = node
        self.end.pre = node

    def remove(self, node: Node) -> None:
        preNode = node.pre
        nxtNode = node.next
        preNode.next = nxtNode
        nxtNode.pre = preNode
    

class  Node:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
    
        
