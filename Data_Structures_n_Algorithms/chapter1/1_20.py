from random import randint

def shuffle(lst):
    for i in range(0, len(lst)):
        x = randint(0, len(lst)-1)
        lst[i], lst[x] = lst[x], lst[i]
       
shuffled = list([1,2,3,4,5,6,7,8,9])
shuffle(shuffled)
print (shuffled)