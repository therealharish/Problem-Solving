class TimeMap:
    def __init__(self):
        self.map = {}
        return None

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key in self.map):
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]
        return None

    def get(self, key: str, timestamp: int) -> str:
        if (key in self.map):
            curr = self.map[key]
        else:
            curr = []
        low = 0
        high = len(curr) - 1
        best = ""
        print(low, high)
        while (low <= high):
            mid = (low + high) // 2
            if (curr[mid][0] <= timestamp):
                best = curr[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        return best


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
