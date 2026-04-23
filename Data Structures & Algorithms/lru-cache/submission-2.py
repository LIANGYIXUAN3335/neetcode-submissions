from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.cacheMap = {}
        self.queue = deque()
        self.capacity = capacity 


    def get(self, key: int) -> int:
        if key in self.cacheMap:
            # 👇 更新顺序
            self.queue.remove(key)
            self.queue.append(key)
            return self.cacheMap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            self.queue.remove(key)
        self.queue.append(key)
        self.cacheMap[key] = value
        length = len(self.queue)
        if length > self.capacity:
            curKey = self.queue.popleft()
            del self.cacheMap[curKey]

