def noRecPermute(n):
    nums = [x for x in range(1, n + 1)]
    s = []
    for i in range (len(nums)):
        s.append(([nums[i], ], nums[:i] + nums[i + 1:]))

    while s:
        soFar, remaining = s.pop()
        if not remaining:
            print(soFar)
        else:
            for i in  range(len(remaining)):
                s.append((soFar + [remaining[i]], remaining[:i] + remaining[i + 1:]))
                
def recPermute(soFar, remaining):
    if not remaining:
        print(soFar)
    for i in range(len(remaining)):
        recPermute(soFar + [remaining[i]], remaining[:i] + remaining[i + 1:])
    

from time import time

start1 = time()
noRecPermute(8)
end1 = time()


pason = [x for x in range(1, 9)]
start = time()
recPermute([], pason)
end = time()
print(end1 - start1)
print(end - start)

# There is barely no performance difference between the rec and norec
# Only disparity is the memory usage