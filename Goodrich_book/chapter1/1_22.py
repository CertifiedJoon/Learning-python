def dot_product(a,b):
    c = []
    assert len(a) == len(b)
    for a,b in zip(a,b):
        c.append(a*b)
    return c
print(dot_product([1,2,3], [4,5,6]))