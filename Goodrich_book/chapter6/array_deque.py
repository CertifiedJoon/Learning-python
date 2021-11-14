class ArrayDeque:
    DEFAULT_CAP = 16
    
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAP
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self._size == 0:
            raise ValueError("Deque is empty, cannot call self.first()")
        return self._data[self._front]
    
    def appendright(self, e):
        if self._size == len(self._data):
            self._resize(2 & len(self._data))
            
        avail = (self._front + self._size) % len(self._data)
        
        self._data[avail] = e
        self._size += 1
        
    def appendleft(self, e):
        if self._size == len(self._data):
            self._resize(2 & len(self._data))
            
        avail = (self._front - 1) % len(self._data)
        self._data[avail] = e
        self._size += 1
        self._front = avail
        
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range (len(old)):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
            
        self._front = 0
        
    def popleft(self):
        if self._size == 0:
            raise ValueError("Deque is empty, cannot popleft")
        
        ret = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ret
    
    def popright(self):
        if self._size == 0:
            raise ValueError("Deque is empty, cannot popleft")
        
        ret = self._data[self._front + self._size - 1]
        self._data[self._front + self._size - 1] = None
        self._size -= 1
        return ret