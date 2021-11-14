import time
import unittest
from collections import defaultdict

def is_rotated_string_sticking(s1, s2):
    return s2 in (s1 + s1)

class test(unittest.TestCase):
    test_cases = [
        ("erbottlewat", "waterbottle", True),
        ("brecarbonfi", "carbonfibre", True),
        ("brecarbonfi", "carbonfiber", False),
        ("watchhand", "handwatch", True),
        ("galaxy", "galaxy", True),
        ("budsear", "earibuds", False)
    ]
    
    test_functions = [
        is_rotated_string_sticking
    ]
    
    def test_is_rotated_string(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for rotated, original, expected in self.test_cases:
                for is_rotated_string in self.test_functions:
                    start = time.process_time()
                    assert(
                    is_rotated_string(rotated, original) == expected
                    ), f"{is_rotated_string.__name__} failed at {rotated} and {original}"
                    function_runtimes[is_rotated_string.__name__] += (
                        time.process_time() - start
                    ) * 1000
                    
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()