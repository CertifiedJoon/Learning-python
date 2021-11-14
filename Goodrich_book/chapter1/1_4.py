def sumsqr(k):
    sum = 0
    
    for i in range (1, k):
        sum += i*i
    
    return sum 

print(sumsqr(10))