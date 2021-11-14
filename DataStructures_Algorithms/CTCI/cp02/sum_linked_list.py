import time
import unittest
from linkedlist import Node, LinkedList
from collections import defaultdict
import random

def sum_linked_list_together(ll1,ll2):
    n1 = ll1.get_head()
    n2 = ll2.get_head()
    digit = 1
    ret = 0
    
    while (n1 != None and n2 != None):
        ret += digit * (n1.get_value() + n2.get_value())
        digit *= 10
        n1 = n1.get_next()
        n2 = n2.get_next()
        
    n = n1 if n1 is not None else n2
    while(n is not None):
        ret += digit * (n.get_value())
        digit *= 10
        n = n.get_next()
        
    return ret 

def sum_linked_list_separate(ll1, ll2):
    n1 = ll1.get_head()
    n2 = ll2.get_head()
    digit = 1
    ret = 0
    
    while (n1 != None):
        ret += digit * (n1.get_value())
        digit *= 10
        n1 = n1.get_next()

    digit = 1
    while (n2 != None):
        ret += digit * (n2.get_value())
        digit *= 10
        n2 = n2.get_next()
        
    return ret

class test(unittest.TestCase):
    test_cases = []
    for _ in range(10):
        test_list1 = random.choices(range(0,10), k = random.choice(range(1,10)))
        test_list2 = random.choices(range(0,10), k = random.choice(range(1,10)))
        expected = (int(''.join(reversed([str(e) for e in test_list1]))) +
                    int(''.join(reversed([str(e) for e in test_list2]))))
        test_cases.append((test_list1, test_list2, expected))
        
    test_functions = [
        sum_linked_list_together,
        sum_linked_list_separate
    ]
    
    def test_sum_linked_list(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for list1, list2, expected in self.test_cases:
                for sum_linked_list in self.test_functions:
                    start = time.process_time()
                    assert(
                        sum_linked_list(LinkedList(list1),
                                       LinkedList(list2)) == expected
                    ), f"{sum_linked_list.__name__} failed at {list1} and {list}"
                    function_runtimes[sum_linked_list.__name__] += (
                    time.process_time() - start ) * 1000
                    
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()
    
    