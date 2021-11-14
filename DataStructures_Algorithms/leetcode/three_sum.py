from collections import defaultdict

def three_sum(nums):
    d = defaultdict(list)
    m = len(nums)
    ret=[]
    check_unique = set()
    for i in range(m - 1):
        for j in range(i + 1, m):
            d[nums[i] + nums[j]].append([i, j])
    for i in range(m):
        for pair in d[-nums[i]]:
            if pair[0] != i and pair[1] != i:
                trio = [nums[pair[0]], nums[pair[1]], nums[i]]
                trio.sort()
                if tuple(trio) not in check_unique:
                    ret.append(trio)
                    check_unique.add(tuple(trio))
    return ret

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1]))