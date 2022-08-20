class Stack():
    #create stack
    def __init__(self,size) -> None:
        self.top = -1 
        self.stack =[None] * size 
        self.size = 0 

    def push(self,value):
        self.top +=1
        self.stack[self.top] = value 
        self.size +=1 
    
    def pop(self):
        if self.isEmpty():
            return None 
        value = self.stack[self.top]
        self.size -= 1
        self.top -=1 
        return value 
    
    def get_size(self):
        return self.size
    
    
    def peek(self):
        return self.stack[self.size]

    def isEmpty(self):
        return not self.size   

    def traverse(self,tranverse_func):
        for i in self.stack:
            tranverse_func(i)
    
    def clear(self):
        self.size = 0 
        self.top = -1 




