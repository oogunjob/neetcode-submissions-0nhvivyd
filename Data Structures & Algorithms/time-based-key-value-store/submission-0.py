class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        if not values:
            return res

        left = 0
        right = len(values) - 1

        while left <= right:
            midpoint = (left + right) // 2

            if values[midpoint][1] <= timestamp:
                res = values[midpoint][0]
                left = midpoint + 1
            else:
                right = midpoint - 1

        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)