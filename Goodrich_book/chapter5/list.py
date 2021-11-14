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
            
    def remove_all(self, val):
        temp = []
        for i in range(self._n):
            if (self._A[i] != val):
                temp.append(self._A[i])
                
        self._A = temp
        self._n = len(temp)
        self._cap = temp.get_cap()
        
    