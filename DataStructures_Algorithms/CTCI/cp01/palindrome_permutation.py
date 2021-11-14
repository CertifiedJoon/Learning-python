import time
import unittest
from collections import defaultdict, Counter

def check_palindromic_permutation_counter(s):
    cnt = Counter((c for c in s if c != " "))
    checked = False
    for val in cnt.values():
        if val % 2 != 0:
            if checked:
                return False
            checked = True
    return True

class Test(unittest.TestCase):
    test_cases = [   vv    
        ("race car", True),
        ("tata coc", True),
        ("doooddd", True),
        ("a", True),
        ("ab", False),
        ("race ccr", False),
        ("rcae cdr", False)
    ]
    
    test_functions = [
        check_palindromic_permutation_counter
    ]
    
    def test_check_palindrome(self):
        num_runs = 1000
        function_runtime = defaultdict(float)

        for _ in range (num_runs):
            for text, expected in self.test_cases:
                for check_palindromic_permutation in self.test_functions:
                    start = time.process_time()
                    assert(
                        check_palindromic_permutation(text) == expected
                    ), f"{check_palindromic_permutation.__name__} failed at {text}"
                    function_runtime[check_palindromic_permutation.__name__] += (                                     time.process_time() - start
                    ) * 1000
                    
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtime.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()