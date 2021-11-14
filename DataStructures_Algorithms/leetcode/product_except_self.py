import time
import unittest
from collections import defaultdict
import random

def product_except_self(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)

    for i in range(len(nums)):
        if i != 0:
            prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(len(nums) - 1, -1, -1):
        if i != len(nums) - 1:
            suffix[i] = suffix[i + 1] * nums[i + 1]
    answer = [prefix[i] * suffix[i] for i in range(len(nums))]
    return answer

def product_except_self_optimized(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)
    for i in range(len(nums)):
        if i != 0:
            prefix[i] = prefix[i - 1] * nums[i -1]
            suffix[-i - 1] = suffix[-i] * nums[-i]
    return [prefix[i] * suffix[i] for i in range(len(nums))]

class Test(unittest.TestCase):
    test_cases = [
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
        ([1,2,3,4,5], [120, 60, 40, 30, 24])
    ]
    test_functions = [
        product_except_self,
        product_except_self_optimized
    ]
    
    def test_two_sums(self):
        num_runs = 10
        function_runtimes = defaultdict(float)
        num_cases = 1000

        for _ in range(num_cases):
            arr = random.choices(range(100), k = random.randrange(100))
            self.test_cases.append((arr, product_except_self(arr)))

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(given) == expected
                    ),f"{solve.__name__} failed at {given}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()