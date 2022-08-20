
class TreeNode : 
    def __init__(self,data=None,left=None,right=None) -> None:
        self.data = data 
        self.left = left 
        self.right = right
    
    def inorderInsert(self,val):
        if self.data :
            if self.data > val :
                if not self.left :
                    self.left = TreeNode(data=val)
                else :
                    self.left.inorderInsert(val)
            else :
                if not  self.right :
                    self.right = TreeNode(data=val)
                else :
                    self.right.inorderInsert(val)
        else :
            self.data = val 
    def insertWithoutRec(self,val):
        temp = self 
        if not temp.data :
            self.data = val 
        # elif temp.data > val and not temp.left  :
        #         temp.left = TreeNode(data=val)
        # elif temp.data <= val and not temp.right :
        #     temp.right = TreeNode(data=val)
        else:
            while temp :
                if  temp.data > val :
                    if not temp.left :
                        temp.left = TreeNode(data=val)
                        break 
                    else :
                        temp = temp.left 
                else :
                    if not temp.right :
                        temp.right = TreeNode(data=val)
                        break 
                    else :
                        temp = temp.right
    
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
    
    
    def depth(self):    
        return max(self.left.depth() if self.left else 0, self.right.depth() if self.right else 0) + 1
    
    
    def size(self):
        return (self.left.size() if self.left else 0 + self.right.size() if self.right else 0 ) + 1
    
    def find(self,val):
        if val == self.data :
            return True 
        else :
            if self.data > val :
                if not self.left:
                    return False 
                return  self.left.find(val)
            else :
                if not self.right:
                    return False 
                return  self.right.find(val)
    
    
    def __str__(self) -> str:
        return f"{self.data}"
    
    





        
mytree = TreeNode(data=10)
# mytree.inorderInsert(20)
# mytree.inorderInsert(20)
# mytree.inorderInsert(5)
mytree.insertWithoutRec(3)
mytree.insertWithoutRec(20)
mytree.insertWithoutRec(20)
mytree.insertWithoutRec(5)
mytree.insertWithoutRec(6)
# print(mytree.depth())
# print(mytree.size())
# print(mytree.left.left)
# mytree.printTree()
print(mytree.delete(200))