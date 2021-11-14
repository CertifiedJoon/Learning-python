import time
import unittest
from collections import defaultdict

def one_edit_away_DC(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    tolerance = 1
    if len(s1) == len(s2):
        for a, b in zip(s1, s2):
            if a != b:
                if not tolerance:
                    return False
                tolerance -= 1
    else:
        i = j = 0
        short, long = (s1, s2) if len(s1) < len(s2) else (s2, s1)
        while (i < len(short) and j < len(long)):
            if short[i] != long[j]:
                if not tolerance:
                    return False
                tolerance -= 1
                j += 1
            else:
                i += 1
                j += 1
    return True

class Test(unittest.TestCase):
    test_cases = [
        # no changes
        ("pale", "pale", True),
        ("", "", True),
        # one insert
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pales", "pale", True),
        ("ples", "pales", True),
        ("pale", "pkle", True),
        ("paleabc", "pleabc", True),
        ("", "d", True),
        ("d", "de", True),
        # one replace
        ("pale", "bale", True),
        ("a", "b", True),
        ("pale", "ble", False),
        # multiple replace
        ("pale", "bake", False),
        # insert and replace
        ("pale", "pse", False),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
        # permutation with insert shouldn't match
        ("ale", "elas", False),
        ("abcdefg", "abcdeff", True),
        ("abcdefg", "abicdefg", True),
        ("abcdefg", "abcdeg", True),
        ("abcdefg", "ddcdefg", False),
        ("abcdefg", "abcccdefg", False),
        ("abcdefg", "abefg", False),
        ("".join(chr(i) for i in range(128)),
        "".join(chr(i//2) for i in range(128)),
        False)
    ]
        
    test_functions = [
        one_edit_away_DC
    ]
    
    def test_one_edit_away(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for s1, s2, expected in self.test_cases:
                for one_edit_away in self.test_functions:
                    start = time.process_time()
                    assert(
                        one_edit_away(s1, s2) == expected
                    ), f"{one_edit_away.__name__} failed at {s1} <-> {s2}"
                    
                    function_runtimes[one_edit_away.__name__] += (
                    time.process_time() - start
                    ) * 1000
                    
        print(f"\n{num_runs} runs")
        for function_name , runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()