import time
import unittest
from collections import defaultdict
from linkedlist import Node, LinkedList
import random

def loop_detection_set(ll):
    nodes = set()
    for e in ll:
        if e in nodes:
            return e 
        nodes.add(e)
    return ll.get_head()

def loop_detection_runner(ll):
    fast = slow = ll.get_head()
    while (fast and fast.get_next()):
        fast = fast.get_next().get_next()
        slow = slow.get_next()
        if (fast == slow):
            break
    if (fast is None or fast.get_next() is None):
        return None
    slow = ll.get_head()
    while (slow != fast):
        slow = slow.get_next()
        fast = fast.get_next()
    return fast

class test(unittest.TestCase):
    test_cases = []
    
    for _ in range(100):
        n1 = random.choice([i for i in range(1,10)])
        ll = LinkedList.generate(n1, 0, 9)
        curr = ll.get_head()
        for i in range(random.choice([i for i in range(n1)])):
            curr = curr.get_next()
        ll.get_tail().set_next(curr)
        test_cases.append((ll, curr))
    
    test_functions = [
        loop_detection_set,
        loop_detection_runner
    ]
    
    def test_loop_detection(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for ll, expected in self.test_cases:
                for loop_detection in self.test_functions:
                    start = time.process_time()
                    assert(
                    loop_detection(ll) == expected
                    ), f"{loop_detection.__name__} failed at {[e.get_value() for e in ll]}, expecting {curr.get_value()}"
                    function_runtimes[loop_detection.__name__] += (
                    time.process_time() - start) * 1000
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<25s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()