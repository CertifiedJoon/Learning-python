from random import randrange
def choice(lst):
    return lst[randrange(len(lst))]

print(choice([k for k in range (10)]))
