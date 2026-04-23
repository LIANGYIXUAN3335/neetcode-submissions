class TimeMap:

    def __init__(self):
        self.timeMap ={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in  self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp,value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        arr = self.timeMap[key]
        left, right = 0, len(arr) - 1
        res = ""  
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] <= timestamp:
                res = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res


