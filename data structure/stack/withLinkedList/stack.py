class StackNode():
    def __init__(self,entry=None,next=None) -> None:
        self.entry = entry 
        self.next = next 


class Stack():
    #create stack
    def __init__(self) -> None:
        self.top = None 
        self.size = 0 

    def push(self,value):
        node  = StackNode(entry=value)
        if not self.top :
            self.top = node
        else:
            node.next = self.top
            self.top = node 
        self.size +=1 
    
    def pop(self):
        value = self.top.entry
        node = self.top 
        self.top = self.top.next 
        del node 
        self.size -= 1
        return value 
    
    def get_size(self):
        return self.size
    
    
    def peek(self):
        return self.top.entry

    def isEmpty(self):
        return not self.top   

    def traverse(self,tranverse_func):
        top = self.top 
        while top  is  not  None :
            tranverse_func(top.entry)
            top = top.next 
    
    def clear(self):
        while self.top  is  not  None :
            node = self.top 
            self.top = self.top.next
            del node 
        
        self.size = 0 
        


mystack = Stack()




