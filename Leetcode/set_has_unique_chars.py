def has_unique_chars(string):
    unique_chars = set()
    for i in string:
        if i in unique_chars:
            return False
        unique_chars.add(i)
    return True

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True