class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.lt = [None]*k
        self.start = 0
        self.end = 0
        self.size = 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size == len(self.lt):
            return False
        self.size+=1
        self.start -= 1
        if self.start < 0:
            self.start += len(self.lt)
        self.lt[self.start] = value
        return True


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.size == len(self.lt):
            return False
        self.size+=1
        self.lt[self.end] = value
        self.end = (self.end + 1) % len(self.lt)
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.size-=1
        self.start = (self.start + 1) % len(self.lt)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.size == 0:
            return False
        self.size -= 1
        self.end -= 1
        if self.end < 0:
            self.end += len(self.lt)
        return True


    def getFront(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.lt[self.start]

    def getRear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.lt[self.end-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.lt)

        


