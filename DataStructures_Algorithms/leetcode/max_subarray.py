import time
import unittest
from collections import defaultdict
import random 
import copy

def max_subarray(nums):
    running = 0
    greatest = float('-inf')
    for n in nums:
        if running <= 0:
            running = n
        else:
            running += n
        if running > greatest:
            greatest = running
    return greatest

def max_subarray_kodane(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
    return max(nums)

class Test(unittest.TestCase):
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6),
        ([1], 1),
        ([5,4,-1,7,8], 23),
    ]
    test_functions = [
        max_subarray,
        max_subarray_kodane
    ]
    
    def test_two_sums(self):
        num_runs = 10
        num_cases = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_cases):
            arr = random.choices(range(100), k = random.randrange(1, 100))
            self.test_cases.append((arr, max_subarray(copy.deepcopy(arr))))

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    copied = copy.deepcopy(given)
                    start = time.process_time()
                    assert(
                        solve(copied) == expected
                    ),f"{solve.__name__} failed at {given}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()