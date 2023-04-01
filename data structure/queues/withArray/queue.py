class Queue():
    def __init__(self,size) -> None:
        self.front = 0
        self.rear = -1 
        self.queue = [None] * size 
        self.size = 0 
        self.queueLength = size 
    
    def isFull(self):
        return self.size == self.queueLength
    
    def isEmpty(self):
        return not self.size 
    
    def queueSize(self):
        return self.size 

    def enqueue(self,value):
        if self.isFull():
            raise Exception("queue is full .")
        self.rear = (self.rear +1) % self.queueLength 
        self.queue[self.rear] = value 
        self.size += 1 
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue is empty .")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.queueLength 
        self.size -=1 
        return value 
    
    def traverse(self,traverse_fun):
        front = self.front  
        for i in range(self.size):
            traverse_fun(self.queue[front])
            front = (front + 1) % self.queueLength
    
    def clear(self):
        self.front = 0 
        self.rear = -1 
        self.size = 0 
    
