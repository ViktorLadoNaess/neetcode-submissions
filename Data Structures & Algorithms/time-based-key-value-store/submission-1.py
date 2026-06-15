from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        d = self.data[key]
        res = ""
        l, r = 0, len(d) - 1
        while l <= r:
            mid = (l + r) // 2
            if d[mid][0] <= timestamp:
                res = d[mid][1]   # valid candidate, look right for a closer one
                l = mid + 1
            else:
                r = mid - 1
        return res
