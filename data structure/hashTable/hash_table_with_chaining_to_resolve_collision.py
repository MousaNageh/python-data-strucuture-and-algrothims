class HashTable:
    def __init__(self,size) -> None:
        self.size = size 
        self.arr = [[] for i in range(size)] 

    def get_hash(self,key):
        key = str(key)
        h = 0 
        for char in key:
            h += ord(char) #asci code (value)
        return h % self.size  # depends on the size og list 
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        found = False
        #if key is exists , then update value
        for index ,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0]==key:
                self.arr[h][index] = (key,value)
                found =True 
                break 
        #push element if not eixits 
        if not found :
            self.arr[h].append((key,value))

    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if len(element) == 2 and element[0] == key:
                return element[1]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        for index ,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0]==key:
                del self.arr[h][index]





