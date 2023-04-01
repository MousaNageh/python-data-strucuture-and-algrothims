import math
class RedixSort:
    def __init__(self,arr:list[int]) -> None:
        self.arr = arr
        self.max_digits = self.__max_digits_in_list()
        self.digit_lists= self.__generate_empty_lists()
        self.__sort()

    def __get_digits_for_number(self,num:int)->int:
        digits:int = 0 
        num = abs(num)
        if num < 9:
            digits = 1 
        else:
            while num >= 1:
                digits +=1 
                num = num // 10
        return digits
    
    def __max_digits_in_list(self)->int:
        results:int  = 0 
        for item in self.arr:
            results = max(results,self.__get_digits_for_number(item)) 
        return results
    
    def __get_number_at_digit(self,num,digit_for_right):
        num = abs(num)
        result = int((num // math.pow(10,digit_for_right)) % 10)
        return result
    
    def __generate_empty_lists(self):
        lists = {}
        for i in range(10):
            lists[i] = []
        return lists
    
    def __make_lists_empty(self):
        for i in range(10):
            self.digit_lists[i] = []
    def __join_lists(self):
        lists = []
        for i in range(9):
            lists = [*lists,*self.digit_lists[i]] 
        self.arr = lists
    

    def __sort(self):
        for i in range(self.max_digits):
            for item in self.arr:
                digit = self.__get_number_at_digit(item,i)
                self.digit_lists[digit].append(item)
            self.__join_lists()
            self.__make_lists_empty()



    
arr =[464,45646456,1,435,765,222222]
sort = RedixSort(arr)
print(sort.arr)