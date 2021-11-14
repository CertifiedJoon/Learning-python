from collections import deque
import queue

def is_valid(s):
    stck = []
    match = {'[': ']', '{': '}', '(':')'}
    for p in s:
        if p not in match and (not stck or match[stck.pop()] != p):
            return False
        else:
            stck.append(p)
    return not stck