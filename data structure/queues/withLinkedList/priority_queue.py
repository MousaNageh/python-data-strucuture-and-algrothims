class QueueNode:
    def __init__(self,entry=None,next=None,priority=None) -> None:
        self.entry = entry 
        self.next =  next 
        self.priority = priority
    def __str__(self) -> str:
        return f"priority:{self.priority},value:{self.entry}"
    

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
            if node.priority >= self.front.priority:
                node.next = self.front 
                self.front = node 
            else:
                front = self.front 
                while front and node.priority < front.priority:
                    front = front.next
                if not front :
                    self.rear.next =node  
                    self.rear = self.rear.next 
                else :
                    node.next = front.next 
                    front.next = node
        self.size +=1 
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("queue is empty .")
        value = self.front.entry 
        front = self.front 
        self.front = self.front.next 
        self.size -=1 
        del front 
        return value 
    
    def traverse(self,traverse_fun):
        front = self.front  
        while front :
            traverse_fun(front.entry)
            front = front.next 
            
    
    def clear(self):
        while self.front:
            self.rear = self.front.next 
            del self.front 
            self.front = self.rear 
        self.size = 0 

myqueue = Queue()
myqueue.enqueue(value=4,priority=5)
myqueue.enqueue(value=10,priority=10)
myqueue.enqueue(value=3,priority=3)
myqueue.enqueue(value=2,priority=2)
myqueue.enqueue(value=20,priority=20)
myqueue.clear()
