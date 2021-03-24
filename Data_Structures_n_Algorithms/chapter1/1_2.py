def is_even(k):
    d, r = divmod(k, 2)
    return True if r == 0 else False

print(is_even(3))