def remove_if_in(s, lst):
    ret = ''
    for c in s:
        if c not in lst:
            ret += c
            
    return ret


lst = ',:;/.'

s = 'lets: have, so;me fun/'

print(remove_if_in(s, lst))
