class Node :
    def __init__(self,data=None,next=None) -> None:
        self.data = data 
        self.next = next 
    def __str__(self) -> str:
        return str(self.data)



class LinkedList:
    def __init__(self) -> None:
        self.head = None 
        self.size = 0
    
    def insert_at_beginning(self,data):
        node = Node(data=data)
        node.next = self.head
        self.head = node    
        self.size +=1
    
    def insert_at_end(self,data):
        node = Node(data=data)
        if not self.head:
            self.head = node 
        else:
            temp = self.head 
            while temp.next :
                temp = temp.next 
            temp.next = node 
        self.size +=1
    
    def insert_at_middle(self,data):
        node = Node(data=data)
        if not self.head:
            self.head = node 
        mid = (self.size-1) // 2
        temp =self.head
        for i in range(mid):
            temp=temp.next 
        node.next = temp.next 
        temp.next = node
        self.size +=1
    
    def insert_at_position(self,data,pos):
        node = Node(data=data)
        if not self.head:
            self.head = node 
        temp =self.head
        i = 0 
        if pos ==0 :
            self.insert_at_beginning(data=data)
        elif pos == self.size -1 :
            self.insert_at_end(data=data)
        else :
            while i < pos -1 : 
                if temp.next :
                    temp=temp.next
                else:
                    break 
                i+=1 
            node.next = temp.next 
            temp.next = node
            self.size +=1
    
    def delete_at_beginning(self):
        if not self.size:
            raise Exception("list is empty .")
        temp = self.head 
        self.head = self.head.next 
        del temp 
        self.size -=1 
    
    def delete_at_end(self):
        if not self.size:
            raise Exception("list is empty .")
        if self.size == 1:
            self.delete_at_beginning()
        else:
            temp=self.head 
            while temp.next.next :
                temp = temp.next 
            to_delete = temp.next
            temp.next=None 
            del to_delete
            self.size -=1
    
    def delete_at_middle(self):
        if not self.size:
            raise Exception("list is empty .")
        if self.size == 1:
            self.delete_at_beginning()
        else :
            mid = (self.size-1) // 2
            temp =self.head
            for i in range(mid):
                if temp.next.next:
                    temp=temp.next 
            to_delete = temp.next 
            temp.next = temp.next.next
            del to_delete
            self.size -=1
    
    def delete_at_position(self,pos):
        if not self.size:
            raise Exception("list is empty .")
        if self.size == 1:
            self.delete_at_beginning()
        elif (self.size - 1) ==pos:
            self.delete_at_end()
        else :
            temp =self.head
            i = 0
            while i < pos - 1: 
                if temp.next :
                    temp=temp.next
                else:
                    break 
                i+=1 
            to_delete = temp.next 
            temp.next = temp.next.next
            del to_delete
            self.size -=1
    
    def search(self,data):
        if not self.size:
            raise Exception("list is empty .")
        temp = self.head
        while temp :
            if temp.data == data:
                return True 
            temp = temp.next
    
    def sort(self):
        if not self.size:
            raise Exception("list is empty .")
        for i in range(self.size-1):
            temp = self.head 
            while temp.next :
                if temp.data > temp.next.data:
                    temp.data,temp.next.data = temp.next.data,temp.data 
                temp =temp.next

    def traverse(self,fun):
        if not self.size:
            raise Exception("list is empty .")
        temp = self.head
        while temp :
            fun(temp.data)
            temp = temp.next 


linked_list = LinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(3)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(4)
linked_list.insert_at_beginning(445)
linked_list.insert_at_beginning(443242)
linked_list.insert_at_beginning(443244534)
linked_list.insert_at_middle(5)
linked_list.insert_at_position(5,0)
linked_list.sort()
# linked_list.delete_at_position(1)

def x(val):
    print(val)

linked_list.traverse(x)
