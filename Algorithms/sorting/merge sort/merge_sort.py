def merge_sort(arr):
    if len(arr) <=1:
        return arr 
    middle = len(arr) // 2 
    left_list = arr[:middle]
    right_list = arr[middle:]
    left_list=merge_sort(left_list)
    right_list=merge_sort(right_list)
    return merge_lists(left_list,right_list)


def merge_lists(left_list,righ_list):
    res = []
    while len(left_list) != 0 and len(righ_list) != 0:

        if left_list[0]<righ_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else :
            res.append(righ_list[0])
            righ_list.remove(righ_list[0]) 
    if len(left_list) != 0 :
        res = res + left_list
    else :
        res = res + righ_list
    print(res)
    return res

# O(n*Log n) 


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(unsorted_list))