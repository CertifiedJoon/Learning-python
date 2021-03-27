n = int(input("input index"))
lst = [k*k for k in range(10)]
try:
    print(lst[n], sep=' ')
except IndexError:
    print("Don't you dare try buffer overflow attacks in python")