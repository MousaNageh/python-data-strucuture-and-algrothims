def bubbleSort(arr):
    arr_len = len(arr) 
    for i in range(0,arr_len-1):
        for j in range(0,arr_len-1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp  


arr = [8,54,324,-23,654,-3453,3423,43234]

bubbleSort(arr)
print(arr)
#O(n²)