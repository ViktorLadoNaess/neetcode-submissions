from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        d = self.d[key]
        if not d:
            return ""
        l, r = 0, len(d) - 1
        while l <= r:
            mid = (l + r) // 2
            t = d[mid][0]
            if t == timestamp:
                return d[mid][1]
            elif t > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return d[r][1] if r >= 0 else ""
