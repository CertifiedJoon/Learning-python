from math import sqrt

def norm(v, p = 2):
    return sum(k*k for k in v) ** (1 / p)
print(norm([3,4]))