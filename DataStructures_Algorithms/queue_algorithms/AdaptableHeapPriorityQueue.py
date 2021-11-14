from HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue._Item):
        __slots__ =  '_index'
        def __init__(self, pos, key, val):
            super().__init__(key, val)
            self._index = pos
    
    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j
    
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
    
    def add(self, k, v):
        token = self.Locator(len(self._data), k, v)
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token
    
    def update(self, loc, k, v):
        j = loc._index
        if not (0 <= j < len(self._data) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        loc._key = k
        loc._value = v
        self._bubble(j)
    
    def remove(self, loc):
        j = loc._index
        if not (0 <= j < len(self._data) and self._data[j] is loc):
            raise ValueError('Invalid locator')
        if j == len(self) - 1:
            self._data.pop()
        else:
            self._swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)
    
if __name__ == '__main__':
    q = AdaptableHeapPriorityQueue()
    q.add(1, "James")
    q.add(2, "Qod")
    q.add(2, "who")
    q.add(0, "Jane")
    q.add(3, "Joon")
    last = q.add(5, "John")
    
    if not q.is_empty():
        key, value = q.get_min()
        print(key, value)
        key, value = q.remove_min()
        print(key, value)
        q.update(last, 0, last._value)
        key, value = q.get_min()
        print(key, value)
        q.remove(last)
        key, value = q.get_min()
        print(key, value)