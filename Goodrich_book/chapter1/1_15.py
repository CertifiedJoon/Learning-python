def is_unique(lst):
    seti = set()
    for num in lst:
        if num in seti:
            return False
        seti.add(num)
    return True

print(is_unique([1,2,3,4,5,6,7,8]))
print(is_unique([1,2,3,4,5,6,7,2]))