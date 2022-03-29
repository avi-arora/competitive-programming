class MaxHeap:

    def __init__(self):
        self.heap = []
        self.size = 0
        

    def parent(self, index):
        """
        Parent of a node always store at i/2 location in binary heap
        """
        return index / 2

    def leftChild(self, index):
        lc = None
        if self.size > 1:
            lc = (2 * index) + 1
        return lc if lc < self.size else None

    def rightChild(self, index):
        rc = None
        if self.size > 2:
            rc = (2 * index) + 2
        return rc if rc < self.size else None

    def maxChild(self, index):
        leftC, rightC = self.leftChild(index), self.rightChild(index)
        max_child = None

        if not leftC and not rightC:
            return None

        if leftC == None: 
            max_child = rightC 
        elif rightC == None:
            max_child = leftC
        elif self.heap[leftC] > self.heap[rightC]:
            max_child = leftC
        else:
            max_child = rightC
        
        return max_child

    def isLeaf(self, index):
        return self.leftChild(index) > self.size \
            and self.rightChild(index) > self.size  

    def correctionUP(self):
        index = self.size // 2
        while index >= 0:
            if not self.isLeaf(index):
                maxCIndex = self.maxChild(index)
                if self.heap[maxCIndex] > self.heap[index]:
                    #swap
                    temp = self.heap[index]
                    self.heap[index] = self.heap[maxCIndex]
                    self.heap[maxCIndex] = temp

            index -= 1

    def correctionDown(self):
        pass

    def percolateUp(self, index):
        while index // 2 > 0:
            #if node is greater than it's parent
            if self.heap[index-1] > self.heap[(index//2)-1]:
                #swap
                temp = self.heap[index-1]
                self.heap[index-1] = self.heap[(index//2)-1]
                self.heap[(index//2)-1] = temp
            index = index // 2
    
    def percolateDown(self, index):
        while (2 * index) < self.size:
            max_child = self.maxChild(index)
            if max_child and self.heap[max_child] > self.heap[index]:
                #swap
                temp = self.heap[index]
                self.heap[index] = self.heap[max_child]
                self.heap[max_child] = temp
            index = max_child


    def insert(self, element):
        self.heap.append(element)
        self.size = self.size+1
        self.percolateUp(self.size-1)

    def getMax(self):
        return self.heap[0]

    def extractMax(self):
        if self.size == 0:
            raise IndexError("no elements in heap.")

        max_elem = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size-1]
            self.heap.pop()
            self.size -= 1
            self.percolateDown(0)
        else:
            self.heap.pop()
            self.size -= 1

        return max_elem
    
    def sort(self):
        pass

    def changePriority(self, position, priority):
        assert self.size < position, "Position cannot exceed size"
        assert self.heap[position] != priority, "Priority cannot be same"

        if priority > self.heap[position]:
            self.increaseKey(position, priority)
        else:
            self.decreaseKey(position, priority)

    def print(self):
        print(self.heap)

    def buildHeap(self, ary):
        """
        build an heap from array
        TimeComplexity: O(n) better than O(nlogn) due to leaf already sorted property. 
        """
        #find parent of first node
        parent = len(ary) // 2
        self.size = len(ary)
        self.heap = [] + ary

        #iterate till root node
        while parent >= 0:
            self.percolateDown(parent)
            parent -= 1

    def increaseKey(self, index, val):
        #validate
        assert self.heap[index] < val, "value should be greater than current element!"

        while index >= 1:
            if self.heap[index] < self.heap[index//2]:
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]
            index = index//2
        

    def decreaseKey(self, index, val):
        #validate 
        assert self.heap[index] > val, "value should be less than of current element!"

        self.heap[index] = val
        while (2 * index) < self.size:
            mxc = self.maxChild(index)
            
            if self.heap[mxc] > self.heap[index]:
                self.heap[mxc], self.heap[index] = self.heap[index], self.heap[mxc]
            index = mxc

class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self, index):
        return index/2

    def leftChild(self, index):
        lc = None
        
        if self.size > 1:
            lc = (2 * index) + 1
        return lc if lc < self.size else None

    def rightChild(self, index):
        rc = None

        if self.size > 2:
            rc = (2 * index) + 2
        return rc if rc < self.size else None

    def minChild(self, index):
        leftC, rightC = self.leftChild(index), self.rightChild(index)
        min_child = None

        if not leftC and not rightC:
            return None
        
        if not leftC:
            min_child = rightC
        elif not rightC:
            min_child = leftC
        elif self.heap[leftC] < self.heap[rightC]:
            min_child = leftC
        else:
            min_child = rightC
        
        return min_child

    def isLeaf(self, index):
        lc, rc = self.leftChild(index), self.rightChild(index)
        return (not lc and not rc) or \
            (lc > self.size and rc > self.size)

    def correctionUp(self):
        index = self.size // 2
        while index >= 0:
            if not self.isLeaf(index):
                minCIndex = self.minChild(index)
                if self.heap[minCIndex] < self.heap[index]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[minCIndex]
                    self.heap[minCIndex] = temp
            index -= 1

    def percolateUp(self, index):
        while index // 2 > 0:
            if self.heap[index-1] < self.heap[(index//2)-1]:
                self.heap[index-1], self.heap[(index//2)-1] = self.heap[(index//2)-1], self.heap[index-1]
            index = index // 2

    def percolateDown(self,index):
        if self.isLeaf(index):
            return
        while (2 * index) <= self.size:
            min_child = self.minChild(index)
            if min_child and self.heap[min_child] < self.heap[index]:
                #swap 
                temp = self.heap[index]
                self.heap[index] = self.heap[min_child]
                self.heap[min_child] = temp
            index = min_child

    def insert(self, element):
        self.heap.append(element)
        self.size = self.size+1
        self.percolateUp(self.size)

    def getMin(self):
        return self.heap[0]

    def extractMin(self):
        if self.size == 0:
            raise IndexError("no elements in heap.")

        min_elem = self.heap[0]
        if self.size > 1:
            self.heap[0] = self.heap[self.size-1]
            self.heap.pop()
            self.size -= 1
            self.percolateDown(0)
        else:
            self.heap.pop()
            self.size -= 1

        return min_elem

    def Sort(self):
        pass

    def changePriority(self, position, priority):
        assert self.size < position, "Position cannot be greater than size"
        assert self.heap[position] != priority, "Priority cannot be same"

        if priority < self.heap[position]:
            self.increaseKey(position, priority)
        else:
            self.decreaseKey(position, priority)


    def print(self):
        print(self.heap)

    def buildHeap(self, ary):
        """
        Build an heap from array, 
        TimeComplexity: O(n)
        """
        #find parent of non-leaf node
        parent = len(ary) // 2
        self.heap = [] + ary
        self.size = len(ary)

        while parent >= 0:
            self.percolateDown(parent)
            parent -= 1
        
        return self.heap

    def increaseKey(self, index, val):
        #validate 
        assert self.heap[index] > val , "value should be less than the current element!"
        self.heap[index] = val
        while index >= 1:

            if self.heap[index] < self.heap[index//2]:
                #swap
                self.heap[index], self.heap[index//2] = self.heap[index//2], self.heap[index]

            index = index // 2        

    def decreaseKey(self, index, val):
        #validate
        assert self.heap[index] < val, "value should be greater than the current element!"

        self.heap[index] = val
        while (2 * index) < self.size:

            mc = self.minChild(index)
            if self.heap[mc] < self.heap[index]:
                self.heap[mc], self.heap[index] = self.heap[index], self.heap[mc]
            
            index = mc
        
            

        
if __name__ == "__main__":
    h = MinHeap()
    a = [5,4,3,2,1]
    h.buildHeap(a)
    h.print()
    h.decreaseKey(0, 10)
    h.print()
