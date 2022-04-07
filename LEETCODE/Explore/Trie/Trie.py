from tkinter import CURRENT
from TrieNode import TrieNodeNAry, TrieNodeDict

class Trie:

    def __init__(self):
        self.root = TrieNodeNAry()
        

    def insert(self, word: str) -> None:
        current = self.root
        for w in word: 
            #get index for w 
            position = ord(w) - ord('a')
            if not current.data[position]:
                current.data[position] = TrieNodeNAry()
                current = current.data[position]
            else:
                #what to do if there's already something in trie
                current = current.data[position]
        current.SetEnd()

    def search(self, word: str) -> bool:
        current = self.root
        for w in word:
            position = ord(w) - ord('a')
            if current and current.data[position]:
                current = current.data[position]
            else:
                return False
        
        return True if current.isEndNode else False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for w in prefix:
            position = ord(w) - ord('a')
            if current and current.data[position]:
                current = current.data[position]
            else:
                return False
        return True


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.search("apple"))
    print(t.search("app"))
    print(t.search("mango"))
    t.insert("april")
    print(t.search("april"))
    
