def shell_sort(arr):
    n = len(arr) 
    increment =  n // 2
    while increment > 0 :
        i = increment 
        for i in range(increment,n):
            key = arr[i]
            j = i - increment
            while j >= 0 and arr[j] > key :
                arr[j+increment] = arr[j]
                j= j - increment
            arr[j+increment] = key          
        increment = increment // 2 
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
shell_sort(unsorted_list)
print(unsorted_list)

# The time complexity of Shell Sort depends on the gap sequence. Its best-case time complexity is O(n* logn) and the worst case is O(n* log2n).