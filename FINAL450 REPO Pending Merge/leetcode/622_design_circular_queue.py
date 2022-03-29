class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = []
        self.front, self.rear = -1, -1
        

    def enQueue(self, value: int) -> bool:
        #check if queue is full or not 
        if self.isFull():
            return False
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        elif (self.rear+1)%self.size < self.front:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = value
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1)%self.size
        return True
        

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1
        

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1
        

    def isEmpty(self) -> bool:
        return (self.rear == -1 and self.front == -1)
        

    def isFull(self) -> bool:
        #return (self.rear+1 == self.front) or (self.rear == -1)
        return (self.rear+1)% self.size == self.front
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()