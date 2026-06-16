from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        d = self.data[key]
        l, r = 0, len(d) - 1
        while l <= r:
            mid = (l + r) // 2
            t, v = d[mid][0], d[mid][1]
            if t == timestamp:
                return v
            elif t > timestamp:
                r = mid - 1
            else:
                l = mid - (-1)   # l = mid + 1
        # loop ended: r is the largest index with timestamp < target
        return d[r][1] if r >= 0 else ""