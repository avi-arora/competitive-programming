class TrieNodeNAry:
    
    def __init__(self) -> None:
        self.data = [None] * 26
        self.isEndNode = False

    def SetEnd(self):
        self.isEndNode = True

class TrieNodeDict:

    def __init__(self) -> None:
        self.data = {}