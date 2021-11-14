import time
import unittest
from collections import defaultdict
import random
from linkedlist import Node, LinkedList

def is_intersecting_runner(ll1, ll2):
    n1 = ll1.get_length()
    n2 = ll2.get_length()
    
    shorter = ll1.get_head() if n1 < n2 else ll2.get_head()
    longer = ll2.get_head() if n2 > n1 else ll1.get_head()
    
    for _ in range(abs(n1 - n2)):
        longer = longer.get_next()
        
    while(shorter != longer):
        shorter = shorter.get_next()
        longer = longer.get_next()

    return bool(longer)

class test(unittest.TestCase):
    test_cases = []
    for i in range(10):
        n1 = random.choice([i for i in range(1, 10)])
        list1 = LinkedList.generate(n1, 0, 9)
        list2 = LinkedList.generate(random.choice([i for i in range(1, 6)]), 0, 9)
        if (i % 2 == 0):
            list2_tail = list2.get_tail()
            intersect_at = list1.get_head()
            for _ in range(random.choice([i for i in range(n1)])):
                intersect_at = intersect_at.get_next()
            list2_tail.set_next(intersect_at)
            list2.set_tail(list1.get_tail())
        test_cases.append((list1, list2, bool(i % 2 == 0)))
    
    test_functions = [
        is_intersecting_runner
    ]
    
    def test_is_intersecting(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        
        for _ in  range(num_runs):
            for l1, l2, expected in self.test_cases:
                for is_intersecting in self.test_functions:
                    start = time.process_time()
                    assert(
                    is_intersecting(l1,l2) == expected
                    ), f"{is_intersecting.__name__} failed at {[e.get_value() for e in l1]} and {[e.get_value() for e in l2]} expecting {expected}"
                    function_runtimes[is_intersecting.__name__] += (
                        time.process_time() - start) * 1000
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()