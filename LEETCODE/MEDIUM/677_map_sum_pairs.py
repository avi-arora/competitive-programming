#using Basic Hashmap and bruteforce
from turtle import position


class MapSumOld:

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

    def sum_oneliner(self, prefix: str) -> int:
        return sum(val for key, val in self.data.items() if key.startswith(prefix))

class TrieNodeNAry:
    def __init__(self) -> None:
        self.data = [None] * 26
        self.val = 0
    
    def SetVal(self, val):
        self.val = val 

class MapSumEfficient:

    def __init__(self):
        self.root = TrieNodeNAry()
        self.ExistedWords = {}
        

    def insert(self, key: str, val: int) -> None:
        current = self.root
        delta = val - self.ExistedWords.get(key, 0)
        for c in key:
            position = ord(c) - ord('a')
            if current and not current.data[position]:
                current.data[position] = TrieNodeNAry()
            
            current = current.data[position]
            current.SetVal(current.val + delta)

        current.SetVal(current.val + delta)
        self.ExistedWords[key] = val

    def sum(self, prefix: str) -> int:
        current = self.root
        for c in prefix:
            position = ord(c) - ord('a')
            if current:
                current = current.data[position]
        
        return current.val if current else 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
