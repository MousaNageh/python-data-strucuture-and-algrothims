def insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i - 1 
        key = arr[i] 
        while j >=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j -=1 
        arr[j+1] = key 

arr = [8,54,324,-23,654,-3453,3423,43234]

insertion_sort(arr)
print(arr)
#O(n²)