def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and target >= arr[i]:
        i = i * 2
    print(arr[i//2:i])
    val = binary_search(arr[i//2:i], target)
    if val == -1:
        return -1
    return (i//2 + val)


def binary_search(arr, target):
    end = len(arr)
    start = 0
    while start <= end:
        mid = (start+end) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


l = [2, 6, 11, 19, 27, 31, 45, 121]
print(exponential_search(l, 121))
