import time
import unittest
from collections import defaultdict
from linkedlist import LinkedList, Node,DoublyLinkedList

def is_palindrome_stringify(ll):
    s = "".join(e.get_value() for e in ll)
    if len(s) < 2:
        return True
    i = 0
    j = len(s) - 1
    while(i <= j):
        if (s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_direct(ll):
    left = ll.get_head()
    right = ll.get_tail()
    while(left != right and right.get_next() != left):
        if (left.get_value() != right.get_value()):
            return False
        left = left.get_next()
        right = right.get_prev()
    return True

class test(unittest.TestCase):
    test_cases = [
        (DoublyLinkedList("racecar"), True),
        (DoublyLinkedList("nolemonsnomelon"), True),
        (DoublyLinkedList("reviver"), True),
        (DoublyLinkedList("d"), True),
        (DoublyLinkedList("raceear"), False),
        (DoublyLinkedList("eeereeee"), False)
    ]
    
    test_functions = [
        is_palindrome_stringify,
        is_palindrome_direct
    ]
    
    def test_is_palindrome(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)
        
        for _ in range(num_runs):
            for ll, expected in self.test_cases:
                for is_palindrome in self.test_functions:
                    start = time.process_time()
                    assert(
                    is_palindrome(ll) == expected
                    ), f"{is_palindrome.__name__} failed at {(e for e in ll)}"
                    function_runtimes[is_palindrome.__name__] += (
                    time.process_time() - start) * 1000
        
        print(f"{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name:<20s}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()