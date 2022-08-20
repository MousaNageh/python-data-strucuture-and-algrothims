from telnetlib import SE


class ListNode :
    def __init__(self) -> None:
        self.next = None 
        self.prev = None 
        self.data = None 
    def __str__(self) -> str:
        return f"{self.data}"

class MyList :
    def __init__(self) -> None:
        self.size = 0 
        self.currentPos = 0 
        self.current = None 
    
    
    def insertList(self ,pos,data):
        node = ListNode()
        node.data = data
        if not self.size :
            self.currentPos = 0 
        elif pos == 0 :
            node.prev = None 
            node.next = self.current 
            self.current.prev = node 
        elif pos >= self.size:
            while self.currentPos < pos-1 :
                self.current = self.current.next 
                self.currentPos +=1 
            node.prev =self.current
            node.next = self.current.next
            self.current.next = node 
        else :
            if pos <= self.currentPos:
                while self.currentPos > pos-1 :
                    self.current = self.current.prev
                    self.currentPos -=1 
            else :
                while self.currentPos < pos - 1 :
                    self.current = self.current.next
                    self.currentPos +=1
            node.prev =self.current
            node.next = self.current.next
            self.current.next.prev =node 
            self.current.next = node
        self.currentPos = pos
        self.current = node 
        self.size +=1 
    
    
    def deleteList(self ,pos): 
        if not self.size or pos > self.size - 1 :
            return 
        elif pos == 0 :
            while self.current.prev:
                self.current = self.current.prev 
            node = self.current 
            self.current.next.prev = None 
            self.current = self.current.next
            del node 
        elif pos == self.size-1 :
            while self.current.next :
                self.current = self.current.next 
            node = self.current 
            self.current.prev.next = None 
            self.current = self.current.prev
            del node 
        else :
            if pos <= self.currentPos:
                while self.currentPos > pos :
                    self.current = self.current.prev
                    self.currentPos -=1
                
            else :
                while self.currentPos < pos  :
                    self.current = self.current.next
                    self.currentPos +=1
            self.current.prev.next = self.current.next 
            self.current.next.prev = self.current.prev 
            node = self.current 
            self.current = self.current.next 
            del node 
        self.currentPos = pos 
        self.size -=1 
    
    def getValue(self,pos):
        postionToRenturn = self.current 
        postion= self.currentPos
        if pos > self.size -1 or pos < 0 or not self.size:
            return 
        elif pos <= postion:
            while postion > pos :
                postionToRenturn = postionToRenturn.prev
                postion -=1
        else :
            while postion < pos  :
                postionToRenturn = postionToRenturn.next
                postion +=1
        return postionToRenturn.data 

mylist = MyList()
mylist.insertList(0,1)
mylist.insertList(0,2)
mylist.insertList(0,3)
mylist.insertList(3,4)
mylist.insertList(2,5)
mylist.insertList(4,6)
print(mylist.getValue(mylist.size-1))