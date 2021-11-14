import queue
class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position:
        """An abstraction representing the location of a single element within a tree.

        Note that two position instaces may represent the same inherent location in a tree.
        Therefore, users should always rely on syntax 'p == q' rather than 'p is q' when testing
        equivalence of positions.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)            # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):                 # works, but O(n^2) worst-case time
        """Return the height of the tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):                  # time is linear in size of subtree
        """Return the height of the subtree rooted at Position p."""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)        # start _height2 recursion

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():                        # use same order as positions()
            yield p.element()
            
    def preorder(self):
        """Generate a preorder iteration of tree's elements.
           Wrapper method for self._rec_preorder(self, p)"""
        if not self.is_empty():
            for c in self._rec_preorder(self.root()):
                yield c
    
    def _rec_preorder(self, p):
        """Generate a preorder iteration of subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._rec_preorder(c):
                yield other
                
    def postorder(self):
        """Generate a postorder iteration of tree's elements.
           Wrapper Method for self._rec_postorder(self, p)"""
        if not self.is_empty():
            for c in self._rec_postorder(self.root()):
                yield c
                
    def _rec_postorder(self, p):
        for c in self.children(p):
            for other in self._rec_postorder(c):
                yield other
        yield p
        
    def preorder_indented(self):
        """
        Print with indents the inorder traversal of the tree.
        Wrapper class for self._rec_preorder_indented(self, p, d)
        """
        self._rec_preorder_indented(self.root(), 0)
        
    def _rec_preorder_indented(self, p, d):
        """Print with indents the inorder traversal of a subtree."""
        print(2*d*' ' + str(p.element()))
        for c in self.children(p):
            self._rec_preorder_indented(c, d + 1)
        
    def breadthfirst(self):
        if not self.is_empty():
            to_visit = [self.root()]
            while to_visit:
                curr = to_visit.pop()
                yield curr
                for child in self.children(curr):
                    to_visit.append(child)
    
    def depthfirst(self):
        if not self.is_empty():
            to_visit = queue.Queue(self.root())
            while to_visit:
                curr = to_visit.get()
                yield curr
                for child in self.children(curr):
                    to_visit.put(child)