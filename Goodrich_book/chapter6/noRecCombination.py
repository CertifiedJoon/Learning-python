from collections import deque

def noRecSubset(s):
    q = deque()
    
    for e in s:
        q.append(e)

    stack = []
    s.append(([q.popleft()], q))
    s.append(([], q))
    
    while s:
        soFar, remaining = s.pop()
        if not remaining:
            print(soFar)
        else:
            s.append((soFar + [q.popleft()], q))
            s.push((soFar, q))