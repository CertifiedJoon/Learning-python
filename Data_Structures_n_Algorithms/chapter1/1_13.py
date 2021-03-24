def reverseordercopy(array):  #This creates a new array (doesn't change the original)
    length = len(array)
    reversed_array = [None]*length
    for i in range(length):
        reversed_array[length-1-i] = array[i]
    return (reversed_array)

def reverseorderinplace(a):  #This performs it in place
    i=0
    l = len(a)
    while i<l//2:
        a[i], a[l-1-i] = a[l-1-i], a[i] #swapping
        i+=1
    return (a)

data = [2,3,5,7,8,4,3,6,7,4,5]
print(reverseordercopy(data))
print(reverseorderinplace(data))
print(list(reversed(data)))


data = [2,3,5,7,8,4,3,6,7,4]
print(reverseordercopy(data))
print(reverseorderinplace(data))
print(list(reversed(data)))


import timeit
result = timeit.timeit("reverseordercopy([2,3,5,7,8,4,3,6,7,4])", number=20000, globals=globals())
print(result)
result = timeit.timeit("reverseorderinplace([2,3,5,7,8,4,3,6,7,4])", number=20000, globals=globals())
print(result)
result = timeit.timeit("reversed([2,3,5,7,8,4,3,6,7,4])", number=20000, globals=globals())
print(result)