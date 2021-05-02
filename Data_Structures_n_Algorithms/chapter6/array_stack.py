class ArrayStack:
    def __init__(self, maxlen=None):
        self._data = [None] * maxlen
        self._size = 0
        self._cap = maxlen
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        if self._size == self._cap:
            temp = [None] * (self._cap * 2)
            for i in range(self._size):
                temp[i] = self._data[i]
            self._data = temp
            self._cap *= 2
            
        self._data[self._size] = e
        self._size += 1
        
    def pop(self):
        if self.is_empty():
            raise ValueError("Cannot pop from empty stack")
        result = self._data[-1]
        self._data[-1] = None
        self._size -= 1
        return result
    
    def top(self):
        if self.is_emtpy():
            raise ValueError("Stack is emtpy")
        return self._data[self._size - 1]
    