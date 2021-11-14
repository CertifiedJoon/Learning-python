import time
import unittest
from collections import defaultdict
import random

def max_profit(prices):
    if not prices:
        raise ValueError("empty list has been passed")
    profits = [0] * len(prices)
    bought = prices[0]
    for i in range(len(prices)):
        if prices[i] - bought < 0:
            profits[i] = 0
            bought = prices[i]
        else:
            profits[i] = prices[i] - bought
    return max(profits)

def max_profit_optimized(prices):
    if not prices:
        raise ValueError("Empy list has been passed")
    profit = 0
    bought = prices[0]
    for price in prices:
        if price - bought <= 0:
            bought = price
        elif price -  bought > profit:
            profit = price - bought
    return profit


class Test(unittest.TestCase):
    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0), 
        ([7,1,5,3,6,4,0], 5),
        ([7,1,5,3,6,4,0,6], 6),
        ([0], 0)
    ]
    test_functions = [
        max_profit,
        max_profit_optimized
    ]
    
    def test_two_sums(self):
        num_runs = 10
        num_cases = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_cases):
            arr = random.choices(range(100), k = random.randrange(1, 100))
            self.test_cases.append((arr, max_profit(arr)))

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(given) == expected
                    ),f"{solve.__name__} failed at {given[0], given[1]}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()