import bisect
from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = SortedDict()
        self.map[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        index = bisect.bisect_right(list(self.map[key].keys()), timestamp) - 1
        if index < 0:
            return ''
        return self.map[key][self.map[key].keys()[index]]
        
