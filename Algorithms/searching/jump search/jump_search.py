import math


def jump_search(arr, target):
    n = len(arr)
    m = int(math.sqrt(n))
    i = 0
    while i < n:
        if arr[i+m-1] == target:
            return i+m-1
        if arr[i+m-1] > target:
            # val = binary_search(arr[i:i+m], target)
            # val = linear_search(arr[i:i+m], target)
            val = interpolation_search(arr[i:i+m], target)

            if val == -1:
                return val
            return i + val

        i += m
    return -1


def linear_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1


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


def interpolation_search(arr, target):
    end = len(arr)-1
    start = 0
    while start <= end:
        mid = start + (((end-start) * (target -
                                       arr[start])) // (arr[end] - arr[start]))
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


l = [2, 6, 11, 19, 27, 31, 45, 121]
print(jump_search(l, 27))

# O(√n)
