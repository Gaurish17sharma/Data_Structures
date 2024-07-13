def first_non_repeating_char(string):
        my_dict = {}
        for i in string:
            my_dict[i] = my_dict.get(i, 0) + 1
            
        for i in string:
            if my_dict[i] == 1:
                return i
                
        return None

print( first_non_repeating_char('leetcode') )
print( first_non_repeating_char('hello') )
print( first_non_repeating_char('aabbcc') )
