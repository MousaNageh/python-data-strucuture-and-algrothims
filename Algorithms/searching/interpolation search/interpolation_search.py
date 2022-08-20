def interploation(arr, target):
    start = 0
    end = len(arr) - 1
    while end >= start:
        mid = start + (((end-start) * (target -
                                       arr[start])) // (arr[end] - arr[start]))
        if arr[mid] == target:
            return True
        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return False


l = [2, 6, 11, 19, 27, 31, 45, 121]
print(interploation(l, 31))

# logn
