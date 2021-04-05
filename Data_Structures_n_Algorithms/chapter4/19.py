def EvenOdd(s, last = 0, index = 0):
    if index == len(s):
        return
    if s[index] % 2 == 0:
        s[last], s[index] = s[index], s[last]
        last += 1
    return EvenOdd(s, last, index + 1)

lst = [1,2,3,4,5,6,6,7,8]
EvenOdd(lst)
print(lst)