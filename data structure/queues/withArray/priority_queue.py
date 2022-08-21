class QueueNode():
    def __init__(self,entry=None,priority=None) -> None:
        self.entry = entry
        self.priority = priority

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
    
    def __insertInToQueue(self,node):
        i = self.rear 
        while i >= self.front :
            if node.priority > self.queue[i].priority  :
                self.queue[i+1] = self.queue[i]
            else:
                break 
            i -= 1
        self.queue[i+1] = node
        self.size += 1 
        self.rear += 1 


    def enqueue(self,value,priority):
        if self.isFull():
            raise Exception("queue is full .")
        node = QueueNode(entry=value,priority=priority)
        if self.front == -1 :
            self.front +=1 
            self.queue[self.rear] = node 
        elif self.rear == self.queueLength - 1  :
            #shift queue 
            i = self.front 
            while i <=self.rear:
                self.queue[i-self.front] = self.queue[i]
                i += 1
            self.rear = self.rear -self.front   
            self.front = 0 
            self.__insertInToQueue(node=node)
        else :
            self.__insertInToQueue(node=node)
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue is empty .")
        value = self.queue[self.front]
        if self.front == self.rear :
            self.front = -1 
            self.rear = 0 
        else :
            self.front +=1 
        self.size -=1 
        return value 
        
    def traverse(self,traverse_fun):
        i = self.front  
        while i <= self.rear :
            traverse_fun(self.queue[i].entry,self.queue[i].priority)
            i+=1 
    
    def clear(self):
        self.front = 0 
        self.rear = -1 
        self.size = 0 

myqueue = Queue(10000)
myqueue.enqueue(1,5)
myqueue.enqueue(14,10)
myqueue.enqueue(16,3)
myqueue.enqueue(18,15)
myqueue.dequeue()

def x(a,b):
    print("value :",a , ", priority :" , b)
myqueue.traverse(x)