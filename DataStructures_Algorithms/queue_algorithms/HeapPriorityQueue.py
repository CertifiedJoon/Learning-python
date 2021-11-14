from PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    def _parent(self, j):
        return (j - 1) // 2
    
    def _left(self, j):
        return j * 2 + 1
    
    def _right(self, j):
        return j * 2 + 2
    
    def _has_left(self, j):
        return len(self._data) > j * 2 + 1
    
    def _has_right(self, j):
        return len(self._data) > j * 2 + 2
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)
    
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            smaller_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smaller_child = right
            if self._data[smaller_child] < self._data[j]:
                self._swap(smaller_child, j)
                self._downheap(smaller_child)
    
    def __init__(self, contents = ()):
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()
    
    def _heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self) - 1)
    
    def get_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
        