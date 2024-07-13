def subarray_sum(nums , target):
    my_dict = {0: -1}
    current_sum = 0
    for i , num in enumerate(nums):
        current_sum = current_sum + num
        if current_sum - target in my_dict:
            return [my_dict[current_sum - target] + 1 , i]
            
        my_dict[current_sum] = i
        
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )