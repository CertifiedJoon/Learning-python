class ArrayQueue:
    DEFAULT_CAP = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAP
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        is self._size == 0:
            raise ValueError("Queue is empty")
            
        return self._data[self._front]
    
    def dequeue(self):
        if self._size == 0:
            raise IndexError("queue is empty")
        
        answer = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        
        return answer
    
    def enqueue(self):
        if len(self._data) == self._size:
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk - self._front
        
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        
        self._front = 0