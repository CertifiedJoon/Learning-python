from binary_tree import BinaryTree
import random
import queue
class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    #-------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_left', '_right' # streamline memory usage

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

  #-------------------------- nested Position class --------------------------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""
    
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    #------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:      # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #-------------------------- binary tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    #-------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:     # left child exists
            count += 1
        if node._right is not None:    # right child exists
            count += 1
        return count

    #-------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = self._Node(e, node)                  # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.

        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = self._Node(e, node)                 # node is its parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node._left if node._left else node._right  # might be None
        if child is not None:
            child._parent = node._parent   # child's grandparent becomes parent
        if node is self._root:
            self._root = child             # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node              # convention for deprecated node
        return node._element
    
    def _attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
            
    def list_by_depth(self):
        """create a list of lists of element in same depth"""
        l = []
        self._rec_list_by_depth(self.root(), 0, l)
        return l

    def _rec_list_by_depth(self, p, depth, l):
        """Create a list of lists of elements in same depth by recursion"""
        if not p:
            return
        if depth >= len(l):
            l.append([])
        l[depth].append(p.element())
        self._rec_list_by_depth(self.left(p), depth + 1, l)
        self._rec_list_by_depth(self.right(p), depth + 1, l)
    
    def _bfs_list_by_depth(self):
        """Create a list of list of elements in same depth by bfs"""
        ret = []
        current =[self.root()]
        while current:
            ret.append([c.element() for c in current])
            parents = current
            current = []
            for parent in parents:
                if self.left(parent):
                    current.append(self.left(parent))
                if self.right(parent):
                    current.append(self.right(parent))
        return ret
    
    def is_balanced(self):
        """check if the tree is balanced"""
        return False if self._rec_is_balanced(self.root()) == float('-inf') else True
    
    def _rec_is_balanced(self, p):
        if p is None:
            return -1
        if self.is_leaf(p):
            return 0
        height_left = self._rec_is_balanced(self.left(p))
        height_right = self._rec_is_balanced(self.right(p))
        if abs(height_left - height_right) > 1:
            return float('-inf')
        return 1 + max(height_left, height_right)
    
    def is_bst(self):
        """Wrapper classs for self._rec_is_bst(p)"""
        return self._rec_is_bst(self.root())
    
    def _rec_is_bst(self, p):
        """Determine whether or not the tree is a binary search tree"""
        if self.is_empty():
            raise ValueError('Tree is empty')
        if self.is_leaf(p):
            return True
        elif not self.left(p) and self.right(p).element() > p.element():
            return self._rec_is_bst(self.right(p))
        elif not self.right(p) and self.left(p).element() < p.element():
            return self._rec_is_bst(self.left(p))
        elif self.left(p).element() < p.element() and self.right(p).element() > p.element():
            return self._rec_is_bst(self.left(p)) and self._rec_is_bst(self.right(p))
        else:
            return False
    
    def inorder_successor(self, p):
        """Find inorder successor of a node at position p"""
        if not isinstance(p, self.Position):
            return ValueError('p is None')
        successor = p
        if not self.right(p):
            while(successor and successor.element() < p.element()):
                successor = self.parent(p)
        else:
            successor = self.right(successor)
            while(self.left(successor)):
                successor = self.left(successor)
        return successor
    
    def common_ancestor(self, p1, p2):
        """Finds the first common ancestor of two nodes given by position p1 and p 2"""
        p1_depth = self.depth(p1)
        p2_depth = self.depth(p2)
        deep, shallow = (p1,p2) if p1_depth > p2_depth else (p2, p1)
        for _ in range (abs(p1_depth - p2_depth)):
            shallow = self.parent(shallow)
        while (deep and shallow):
            if deep == shallow:
                return shallow
            else:
                deep = self.parent(deep)
                shallow = self.parent(shallow)
        return None
    
    def check_subtree(self, root1, root2):
        """checks if root2 is a subtree of root2"""
        if not root1 or not root2:
            return False
        curr = root2
        while curr:
            if curr == root1:
                return True
            curr = self.parent(curr)
        return False
    
    def randnode(self):
        """gets random node from the tree"""
        r = random.randrange(len(self))
        q = queue.Queue()
        q.put(self.root())
        while q:  
            n = q.get()
            if not r:
                return n
            r -= 1
            for c in self.children(n):
                if c:
                    q.put(c)
        return None
    
    def count_path_sum(self, k):
        """Counts how many paths(a link of two nodes or more) sum to k"""
        if self.is_empty():
            return 0
        cnt = 0
        def backtracking(p, path_sums):
            """backtracking method for summing the nodes. path variable allows the backtracking function to know if path has already been visited"""
            nonlocal cnt
            if p is None:
                return
            
            new_sum = [c + p.element() for c in path_sums]
            new_sum.append(p.element())
            cnt += new_sum[:-1].count(k)
            
            if self.left(p):
                backtracking(self.left(p), new_sum)
            if self.right(p):
                backtracking(self.right(p), new_sum)
                
        backtracking(self.root(), [])
        return cnt