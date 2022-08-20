def selection_sort(arr):
    n = len(arr)
    for i in  range(n):
        for j in range(i,n):
            if arr[j]<arr[i]:
                arr[j],arr[i]= arr[i],arr[j]

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(unsorted_list)
print(unsorted_list)
# O(n2)