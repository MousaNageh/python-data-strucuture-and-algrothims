class QueueNode:
    def __init__(self,entry=None,next=None,priority=None) -> None:
        self.entry = entry 
        self.next =  next 
        self.priority = priority
    

class Queue():
    def __init__(self) -> None:
        self.front = None 
        self.rear = None 
        self.size =  0 
    
    def isFull(self):
        return False 
    
    def isEmpty(self):
        return not self.size 
    
    def queueSize(self):
        return self.size 

    def enqueue(self,value,priority):
        node  = QueueNode(entry=value,priority=priority)
        if not self.front:
            self.front = node 
            self.rear = node 
        else:
            self.rear.next = node  
            self.rear = self.rear.next 
        self.size +=1 
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue is empty .")
        value = self.front.entry 
        node  = self.front 
        self.front = self.front.next 
        self.size -=1 
        del node 
        return value 
    
    def traverse(self,traverse_fun):
        front = self.front  
        while front is not None:
            traverse_fun(front.entry)
            front = front.next 
    
    def clear(self):
        while self.front is not None:
            self.rear = self.front.next 
            del self.front 
            self.front = self.rear 
        self.size = 0 

myqueue = Queue()

