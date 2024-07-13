def find_duplicates(nums):
    my_dict = {}
    for i in nums:
        my_dict[i] = my_dict.get(i , 0) + 1
        
    duplicates = []
    
    for i , count in my_dict.items():
        if count > 1:
            duplicates.append(i)
            
    return duplicates

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )