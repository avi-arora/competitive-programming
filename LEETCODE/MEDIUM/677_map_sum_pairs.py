#using Basic Hashmap and bruteforce
class MapSum:

    def __init__(self):
        self.data = {}
        

    def insert(self, key: str, val: int) -> None:
        self.data[key] = val
        

    def sum(self, prefix: str) -> int:
        result = 0
        for key, value in self.data.items():
            if key.startswith(prefix):
                result += value
        return result