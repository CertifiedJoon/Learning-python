import time
import unittest
from collections import defaultdict, Counter

def check_permutation_BF(s1, s2):
    """
    A BruteForce algorithm that runs in O(n * n!) time
    and O(n!) space
    """
    if (len(s1) != len(s2)): 
        return False
    
    ret = set()
    rec_permute("", s2, ret)
    if s1 in ret:
        return True
    return False

def rec_permute(so_far, remaining, ret):
    if not remaining:
        ret.add(so_far)
        return
    for i in range(len(remaining)):
        rec_permute(
            so_far + remaining[i], 
            remaining[:i] + remaining[i+1:],         
            ret)
        
def check_permutation_dict(s1, s2):
    """
    Utilizes O(n) space to achieve O(n) time.
    Mimic a multiset using a dict with a key count as val
    """
    if len(s1) != len(s2):
        return False
    
    c_cnt = map_c_cnt(s1)
    for c in s2:
        if c_cnt.get(c, 0) == 0:
            return False
        c_cnt[c] -= 1
    return True

def map_c_cnt(s):
    ret = dict()
    for c in s:
        ret[c] = ret.get(c, 0) + 1;
    return ret

def check_permutation_counter(s1, s2):
    """
    For pythonic Code, import Counter class from colections
    to utilize multiset/dict counter
    """
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)

class Test(unittest.TestCase):
    test_cases = [
        ("abcdefg", "abcdefg", True),
        ("", "", True),
        ("abbccdddeee", "abcbcddeede", True),
        ("12341234","43211234", True),
        ("123f 2fd", "123 f2df", True),
        ("asdfg", "aasdg", False),
        ("qwerasdfzxcv", "qwercsdfzxcd", False),
        ("".join(chr(i) for i in range(128)),
         "".join(chr(i) for i in reversed(range(128))),
         True)
    ]
    
    test_functions = [
        # check_permutation_BF,
        check_permutation_dict,
        check_permutation_counter
    ]
    
    def test_check_permutation(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for s1, s2, expected in self.test_cases:
                for check_permutation in self.test_functions:
                    start = time.process_time()
                    assert(
                        check_permutation(s1,s2) == expected
                    ), f"{check_permutation.__name__} failed for {s1} <-> {s2}"
                    function_runtimes[check_permutation.__name__] += (
                        time.process_time() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<15s}: {runtime:.1f}ms")
        
if __name__ == "__main__":
    unittest.main()