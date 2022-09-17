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
    
    def add (self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value 
    

    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def delete(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

myTable = HashTable(10)
myTable[1] = 1 
# del myTable[1]
# myTable['1'] = 2
print(myTable[1])



