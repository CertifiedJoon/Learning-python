def odd_pair_in(lst):
    for num1 in [k for k in lst if k%2 == 1]:
        for num2 in [j for j in lst if j % 2 == 1 and j != num1]:
            return True
    return False

print(odd_pair_in([1,2,4,6,7]))