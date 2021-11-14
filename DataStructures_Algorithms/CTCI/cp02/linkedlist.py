import random

class Node:
    def __init__(self, val, next_node=None, prev_node=None):
        self._val = val
        self._next_node = next_node
        self._prev_node = prev_node
    def get_next(self):
        return self._next_node
    
    def set_next(self, node):
        self._next_node = node
        
    def get_value(self):
        return self._val
    
    def set_value(self, val):
        self._val = val
        
    def get_prev(self):
        return self._prev_node
    
    def set_prev(self, val):
        self._prev_node = val
        
class LinkedList:
    def __init__(self, initializers = None):
        self._head = None
        self._tail = None
        if initializers is not None:
            self.add_multiple(initializers)
            
    def __iter__(self):
        current = self._head
        while(current != None):
            yield current
            current = current.get_next()
            
    def get_head(self):
        return self._head
    
    def get_tail(self):
        return self._tail
    
    def set_tail(self, new_tail):
        self._tail = new_tail
    
    def get_length(self):
        length = 0
        curr = self._head
        while(curr is not None):
            length += 1
            curr = curr.get_next()
        return length
    
    def add(self, e):
        if isinstance(e, Node):
            if self._head == None:
                self._head = e
            else:
                self._tail.set_next(e)
            self._tail = e
        else:
            new_node = Node(e)
            if self._head == None:
                self._head = new_node
            else:
                self._tail.set_next(new_node)
            self._tail = new_node
                
    def add_multiple(self, elements):
        for e in elements:
            self.add(e)
            
    @classmethod
    def generate(cls, k, min_value, max_value):
        return cls(random.choices(range(min_value, max_value), k=k))
    
class DoublyLinkedList(LinkedList):
    def add(self, e):
        if isinstance(e, Node):
            if self._head == None:
                self._head = e
            else:
                self._tail.set_next(e)
                e.set_next(self._tail)
            self._tail = e
        else:
            new_node = Node(e)
            if self._head == None:
                self._head = new_node
            else:
                self._tail.set_next(new_node)
                new_node.set_prev(self._tail)
            self._tail = new_node