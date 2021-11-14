def merge(s1, s2, s):
    i = j = 0
    while i < len(s1) or j < len(s2):
        if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
            s[i + j] = s1[i]
            i += 1
        else:
            s[j + i] = s2[j]
            j += 1

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0: mid]
    s2 = s[mid: n]
    
    merge_sort(s1)
    merge_sort(s2)

    merge(s1, s2, s)

def bottom_up_merge_sort(s):
    m = 1
    low = 0
    high = len(s) - 1
    
    while m < high - low:
        for i in range(low, high, m * 2):
            frm = i
            mid = i + m
            to = min(i + m * 2 - 1, high)
            s1 = s[frm: mid]
            s2 = s[mid: to + 1]
            merge(s1, s2, s[frm: to + 1])
        m *= 2

def quick_sort(s):
    rec_quick_sort(s, 0, len(s) - 1)

def rec_quick_sort(s, l, r):
    if l >= r:
        return
    mid = l + (r - l) // 2
    s[mid], s[l] = s[l], s[mid]
    last = l
    i = l
    while i <= r:
        if s[i] < s[l]:
            last += 1
            s[last], s[i] = s[i], s[last]
        i += 1
    s[last], s[l] = s[l], s[last]
    
    rec_quick_sort(s, l, mid - 1)
    rec_quick_sort(s, mid + 1, r)

def optimized_quick_sort(s):
    inplace_quick_sort(s, 0, len(s) - 1)

def inplace_quick_sort(s, a, b):
    if a >= b:
        return
    left = a
    pivot = s[b]
    right = b - 1
    while left <= right:
        while left <= right and s[left] < pivot:
            left += 1
        while left <= right and pivot < s[right]:
            right -= 1
        if left <= right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
    s[left], s[b] = s[b], s[left]
    inplace_quick_sort(s, a, left - 1)
    inplace_quick_sort(s, left + 1, b)

def sort_default(s):
    s.sort()

import unittest
import time
import random
from collections import defaultdict
import copy
class Test(unittest.TestCase):
    test_cases = []
    test_functions = [
        merge_sort,
        bottom_up_merge_sort,
        quick_sort,
        optimized_quick_sort,
        sort_default
    ]
    def test_sort(self):
        for _ in range(40):
            arr = random.choices(range(100), k = 2000)
            expected = sorted(arr)
            self.test_cases.append((arr, expected))
        
        num_runs = 10
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for arr, expected in self.test_cases:
                copied = copy.deepcopy(arr)
                for sort in self.test_functions:
                    start = time.process_time()
                    sort(copied)
                    assert(
                        copied == expected
                    ), f"{sort.__name__} failed at {arr}"
                    function_runtimes[sort.__name__] += (
                        time.process_time() - start
                    ) * 1000
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()