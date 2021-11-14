import unittest
import random

class myQueue:
    def __init__(self):
        self._s1 = []
        self._s2 = []
        
    def add(self, e):
        while self._s1:
            self._s2.append(self._s1.pop())
        self._s1.append(e)
        while self._s2:
            self._s1.append(self._s2.pop())
            
    def pop(self):
        return self._s1.pop()
    
    def __iter__(self):
        while self._s1:
            yield self._s1.pop()
    
class Test(unittest.TestCase):
    test_cases = []
    
    for _ in range(10):
        test_cases.append(random.choices(range(10), k = random.randrange(1, 10)))
    
    def test_add_pop(self):
        num_runs = 1000
        for _ in range(num_runs):
            for test_list in self.test_cases:    
                q = myQueue()
                for e in test_list:
                    q.add(e)
                result = [popped for popped in q]
                assert(test_list == result), f"myQueue failed at {test_list} --> {result}"
        
        print(f"{num_runs} runs")
        
if __name__ == "__main__":
    unittest.main()