def QuickStep(s, k, last = 0, index = 0):
    if (index == len(s)):
        return
    
    if (s[index] < k):
        s[index], s[last] = s[last], s[index]
        last += 1
        
    return QuickStep(s, k, last, index + 1)


lst = [1,2,3,43,4,3,4,32,3]
QuickStep(lst, 10)
print(lst)