import time
import unittest
from collections import defaultdict

def string_compress(s):
    compressed = []
    if not s: 
        return s
    current_chr = s[0]
    current_count = 0
    for c in s:
        if current_chr == c:
            current_count += 1
        else:
            compressed.extend([current_chr, current_count])
            current_chr = c
            current_count = 0
    print("".join((str(e) for e in compressed))) 
    return "".join((str(e) for e in compressed)) if len(compressed) < len(s) else s

class Test(unittest.TestCase):
    testcases = [
        ("aabbccc", "a2b2c3"),
        ("aaabbbccc", "a3b3c3"),
        ("abcdefg","abcdefg"),
        ("abbbbbbbc", "a1b6c1")
    ]
    
    test_functions = [
        string_compress
    ]
    
    def test_string_compress(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for text, expected in self.testcases:
                for compresser in self.test_functions:
                    start = time.process_time()
                    assert(
                        compresser(text) == expected
                    ), f"{compresser.__name__} failed at {text}"
                    function_runtimes[compresser.__name__] += (
                    time.process_time() - start
                    ) * 1000
        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")
        
        
if __name__ == "__main__":
    unittest.main()