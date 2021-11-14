import time
import unittest
from collections import defaultdict

def is_anagram(s, t):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    for c in t:
        d[c] -= 1
    return not any(d.values())

class Test(unittest.TestCase):
    test_cases = [
        (['anagram', 'anarmga'], True),
        (['rat', 'tar'], True),
        (['races', 'cesar'], True),
        (['afsds', 'sdfs'], False),
        (['rat', 'car'], False),
        (['andf', 'a'], False),
    ]
    test_functions = [
        is_anagram
    ]
    
    def test_two_sums(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for given, expected in self.test_cases:
                for solve in self.test_functions:
                    start = time.process_time()
                    assert(
                        solve(given[0], given[1]) == expected
                    ),f"{solve.__name__} failed at {given[0]}"
                    function_runtimes[solve.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()