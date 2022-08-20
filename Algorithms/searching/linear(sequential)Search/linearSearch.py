#O(n)
def linearSearch(arr,val):
    for i in range(len(arr)):
        if arr[i] == val :
            return i 
    return -1 

arr = [1,45,56,45,34,34,5,655,45,45,54,5,45]

print(linearSearch(arr,34)) #4
