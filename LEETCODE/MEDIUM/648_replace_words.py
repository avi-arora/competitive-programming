class TrieNodeNAry:
    def __init__(self):
        self.data = [None] * 26
        self.isEnd = False
        
    def SetEnd(self):
        self.isEnd = True

class Solution:
    def __init__(self):
        self.root = TrieNodeNAry()
    
    def insert(self, word):
        current = self.root
        for c in word:
            position = ord(c) - ord('a')
            if current and not current.data[position]:
                current.data[position] = TrieNodeNAry()
            current = current.data[position]
        current.SetEnd()
    
    def GetWordPrefix(self, word):
        result = ""
        current = self.root
        for c in word:
            position = ord(c) - ord('a')
            if current and current.data[position]:
                result += c
                current = current.data[position]
            elif (not current.isEnd):
                return ""
            
            if current.isEnd:
                return result
            
        return result

    def replaceWords(self, dictionary: [str], sentence: str) -> str:
        #build trie
        for word in dictionary:
            self.insert(word)
        result = []
        for word in sentence.split(" "):
            rootWord = self.GetWordPrefix(word)
            if rootWord != "":
                result.append(rootWord)
            else:
                result.append(word)
        return " ".join(result)
            
                