class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        self.topStack = -1
        self.topMin = -1
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.topMin == -1:
            self.minStack.append(x)
            self.topMin += 1
        elif self.topMin >= 0 and x <= self.minStack[self.topMin]:
            self.minStack.append(x)
            self.topMin += 1
        self.topStack+= 1    
            
    def pop(self) -> None:
        elem = self.stack.pop()
        self.topStack -= 1
        if elem == self.minStack[self.topMin]:
            self.minStack.pop()
            self.topMin -= 1
        

    def top(self) -> int:
        if self.topStack >= 0:
            return self.stack[self.topStack]
        return self.topStack
        

    def getMin(self) -> int:
        if self.topMin >= 0:
            return self.minStack[self.topMin]
        return self.topMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()