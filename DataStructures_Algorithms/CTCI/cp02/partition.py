import time 
import unittest
from collections import defaultdict
from linkedlist import Node, LinkedList
from copy import deepcopy

def partition_linked_list(ll, element):
    left = last = ll.get_head()
    while(left.get_value() != element):
        left = left.get_next()
    swap(left, ll.get_head())
    for e in ll:
        if e.get_value() < ll.get_head().get_value():
            last = last.get_next()
            swap(e, last)
    swap(last, ll.get_head())
    return ll

def swap(node1, node2):
    temp = node2.get_value()
    node2.set_value(node1.get_value())
    node1.set_value(temp)

class test(unittest.TestCase):
    def test_partition_linked_list(self):
        num_runs = 1000
        function_runtime = 0
        
        for _ in range(num_runs):
            start = time.process_time()
            ll = LinkedList.generate(10,0,100)
            partition_linked_list(ll, ll.get_head().get_value())
            function_runtime += (time.process_time() - start) * 1000
        
        print(f"{num_runs} runs at {function_runtime:.1f}ms")
if __name__ == "__main__":
    unittest.main()