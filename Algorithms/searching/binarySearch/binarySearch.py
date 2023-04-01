#**************** recursion  ********************* 
# O(log n) 


def recBinarySearch(val,arr,start,end):
    if start <= end :
        middle =  (start+end) // 2
        if arr[middle] == val: 
            return middle
        elif arr[middle] > val :
            return recBinarySearch(val,arr,start,middle-1)
        else :
            return recBinarySearch(val,arr,middle+1,end)
    return -1

def binarySearch(val,arr):
    return recBinarySearch(val,arr,0,len(arr)-1)


#************* iterative ****************

def iteravtiveBinarySearch(val,arr):
    start = 0 
    end =  len(arr) -1  
    middle = None
    while start <= end :
        middle = (start+end) // 2 
        if arr[middle] == val :
            return middle 
        elif arr[middle] > val :
            end = middle - 1 
        else :
            start = middle + 1 
    return -1 

#**********
arr = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(71,arr))
print(iteravtiveBinarySearch(71,arr))