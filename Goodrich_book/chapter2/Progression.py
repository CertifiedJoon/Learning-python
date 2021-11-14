from math import sqrt
class Progression:
    """Iteartor producing a generic progression"""
    
    def __init__(self, start=0):
        self._current = start
        
    def _advance (self):
        self._current += 1
        
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def __iter__(self):
        return self
    
    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))
        
class FibonacciProgression(Progression):
    
    def __init__(self, first=2, second=200):
        
        super().__init__(first)
        self._prev = second - first # fictitious value representing the value before first (for the purpose of iteration)
        
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current
        
        
class ReverseFibonnaciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first
    
    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev)
        
class SquareRootProgression(Progression):
    def __init__(self, current = 65536):
        super().__init__(current)
        
    def _advance(self):
        self._current = sqrt(self._current)

fibo = FibonacciProgression(2, 2)
fibo.print_progression(8)