def two_sum(nums , target):
    my_dict = {}
    for i , num in enumerate(nums):
        second_num = target - num
        
        if second_num in my_dict:
            return [my_dict[second_num] , i]
            
        my_dict[num] = i
        
    return []
    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9)) 