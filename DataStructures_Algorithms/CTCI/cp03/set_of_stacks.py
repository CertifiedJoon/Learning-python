import unittest

class SetOfStacks:
    def __init__(self, capacity):
        self._capacity = capacity 
        self._stacks = [[]]
    
    def add(self, value):
        if (len(self._stacks[-1]) >= self._capacity):
            self._stacks.append([value,])
        else:
            self._stacks[-1].append(value)
    
    def pop(self):
        if not self._stacks[-1]:
            self._stacks.pop()
        return self._stacks[-1].pop()
    
    def is_empty(self):
        return (len(self._stacks[0]) == 0)
    
    def top(self):
        return self._stacks[-1][-1]
    
class test(unittest.TestCase):   
    def test_SOS(self):
        sos = SetOfStacks(5)
        for i in range(30):
            sos.add(i)
        lst = []
        while not sos.is_empty():
            lst.append(sos.pop())
        return sos == reversed([i for i in range(30)])
    
if __name__ == "__main__":
    unittest.main()