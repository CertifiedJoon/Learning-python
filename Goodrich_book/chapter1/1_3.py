def minmax(lst):
    maxi = mini = lst[0]
    for num in lst:
        if (num < mini):
            mini = num
        elif (num > maxi):
            maxi = num
    return mini, maxi


print(minmax((1,2,3,4,5,5,6,6,0)))