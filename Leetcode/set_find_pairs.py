def find_pairs(arr1 , arr2 , target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        second_num = target - num
        if second_num in set1:
            pairs.append((second_num , num))
            
    return pairs
            
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)