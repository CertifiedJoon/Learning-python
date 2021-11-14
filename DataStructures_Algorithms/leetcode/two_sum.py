import time
import unittest
from collections import defaultdict

def two_sums_dictionary(nums, target):
    d = {}
    for i,n in enumerate(nums):
        if target-n in d:
            return [d[target-n], i]
        d[n] = i
    raise RuntimeError('Not Found')
        

def two_sums_sort(nums, target):
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)):
        j = binary_search_except(sorted_nums, target - sorted_nums[i], i)
        if j != -1:
            return find_two(nums, sorted_nums[i], sorted_nums[j])

def find_two(nums, a, b):
    ret = []
    found_a = False
    found_b = False
    for i in range(len(nums)):
        if not found_a and nums[i] == a:
            found_a = True
            ret.append(i)
        elif not found_b and nums[i] == b:
            found_b = True
            ret.append(i)
    return ret

def binary_search_except(nums, target, excpt):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if nums[mid] == target and mid != excpt:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def two_sums_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

class Test(unittest.TestCase):
    test_cases = [
        ([[2, 7, 11, 15], 9], [0, 1]),
        ([[3, 2, 4], 6], [1, 2]),
        ([[3, 3], 6], [0, 1]),
        ([[2, 7, 11, 15, 20, 35, 36, 143, 342, 343, 32434, 234424], 32777], [9, 10]),
        ([[2, 7, 11, 15, 20, 35, 36, 143, 342, 343, 32434, 234424], 234426,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], [0, 11]),
        ([[2, 7, 11, 15, 20, 35, 36, 143, 342, 343, 32434, 234424, 1235352,123563426,12312546,34321456547654,324213462346,23452345234623452,2435234523461234523452345], 71], [5, 6])
    ]
    test_functions = [
        two_sums_sort,
        two_sums_brute_force,
        two_sums_dictionary
    ]
    
    def test_two_sums(self):
        num_runs = 10000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(given[0], given[1]) == expected
                    ),f"{solve.__name__} failed at {given[0], given[1]}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()