class list:
    def __init__(self):
        self._n = 0
        self._cap = 1
        self._A = self._make_array(self._cap)
        
    def _make_array(self, cap):
        return (capacity * ctypes.py_object)()
    
    def pop(self):
        if not self._n:
            raise IndexError('Cannot pop from an empty array')
        self._A[self._n - 1] = None
        self._n -= 1
        
        if (self._n <= self._cap // 4):
            B = self._make_array(self._n * 2)
            for i in range (self._n):
                B[i] = self._A[i]
                
            self._A = B
            self._cap = self._n * 2
            
    