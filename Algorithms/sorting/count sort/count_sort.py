"""
-> O(n) 
-> there are two arrays , one (count array) includes number of occurence and the length of this array 
    is the largest number in the input array  , other (output array) one is the output array 
    example : 
       input array = [2,4,5,3,9,1,10]
       so the largest number is 10 , count array will be 10 elements (10 length)
-> if we will sort charcters ,then count array will be 256 (ASCI code) of characters
-> every index in count array will includes number of occurence of the element of the input array 
    example :
        input array = [2,4,5,3,9,1,10,9,2,3,5]
        count array = [1,2,2,1,2,0,0,0,2,1]
-> every element in count array will add to previous one 
-> occurence of element in count array will be index of the element in output array 
-> reduce occurence by one 

"""
def count_sort(arr):
    largest_value = 0 
    #find largest values in array 
    for item in arr:
        if item > largest_value:
            largest_value = item
    # create count array with length of largest values
    count = [0 for i in range(largest_value+1)]
    output = [None for i in range(len(arr))]
    # count number of occurence 
    for i in arr :
        count[i] +=1 
    # sum every count element with next one
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for item in arr :
        output_index = count[item]
        #as index start with one 
        output[output_index-1] = item
        count[item] -=1 
    return output


print(count_sort([2,4,5,3,9,1,10,9,2,3,5]))

def count_sort_string(arr):
    largest_value =256 
    # create count array with length of largest values
    count = [0 for i in range(256)]
    output = ["" for i in range(len(arr))]
    # count number of occurence 
    for i in arr :
        count[ord(i)] +=1 
    # sum every count element with next one
    for i in range(1,len(count)):
        count[i] += count[i-1]
    for item in arr :
        output_index = count[ord(item)]
        #as index start with one 
        output[output_index-1] = item
        count[ord(item)] -=1 
    return "".join(output)
print(count_sort_string("mousanageh"))