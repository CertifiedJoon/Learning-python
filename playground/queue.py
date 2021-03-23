class Queue(object):
    def __init__(self, head = None):
        self.q = [head]
    
    def enqueue(self, new_elem):
        self.q.append(new_elem)
        pass

    def deque(self):
        return self.q.pop(0)
    
    def peek(self):
        return self.q[0]


q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print q.peek()

# Test dequeue
# Should be 1
print q.dequeue()

# Test enque    
q.enqueue(4)
# Should be 2
print q.dequeue()
# Should be 3
print q.dequeue()
# Should be 4
print q.dequeue()
q.enqueue(5)
# Should be 5
print q.peek()
