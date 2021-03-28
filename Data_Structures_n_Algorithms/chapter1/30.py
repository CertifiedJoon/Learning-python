def halves_to_two(k):
    cnt = 0
    d = k / 1
    while(d >= 2):
        d /= 2
        cnt += 1
    return cnt

print(halves_to_two(2))