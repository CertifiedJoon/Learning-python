import time
import unittest
from collections import defaultdict

def sort_stack_bf(stack):
    if not stack:
        return True
    temp = [stack.pop(),]
    while not is_sorted(stack, temp):
        while stack:
            if stack[-1] >= temp[-1]:
                temp.push(stack.pop())
            else:
                pop_swap = temp.pop()
                temp.append(stack.pop())
                stack.append(temp.pop())
    return stack

def is_sorted(recipient, delivery):
    print(recipient, delivery)
    prev = delivery.pop()
    recipient.append(prev)
    is_stack_sorted = True
    while delivery:
        curr = delivery.pop()
        if curr > prev:
            is_stack_sorted = False
        recipient.append(curr)
    return is_stack_sorted

class Test(unittest.TestCase):
    test_cases = [
        ([0,1,2,3,4,5,6,7,8], [8,7,6,5,4,3,2,1,0]),
        ([4,3,5,7,2,1], [1,2,3,4,5,7]),
        ([0],[0]),
        ([3,4,5,2,4,23,6,4,2,5,7], [2,2,3,4,4,4,5,5,6,7,23])
    ]
    
    test_functions = [
        sort_stack_bf
    ]
    
    def test_sort_stack(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        for _ in range(num_runs):
            for unsorted, expected in self.test_cases:
                for sort_stack in self.test_functions:
                    start = time.process_time()
                    assert(
                    sort_stack(unsorted) == expected
                    ),f"{sort_stack.__name__} failed at {unsorted}"
                    function_runtimes[sort_stack.__name__] += (
                    time.process_time() - start) * 1000
        
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print("{function_name:<24s}: {runtime:.1f}ms")
            
if __name__ == "__main__":
    unittest.main()