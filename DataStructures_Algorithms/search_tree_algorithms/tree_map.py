import random
import sys 
import os
sys.path.append(os.path.abspath("/home/coder/Algorithms/map_algorithms"))
from MapBase import MapBase
sys.path.remove(os.path.abspath("/home/coder/Algorithms/map_algorithms"))
sys.path.append(os.path.abspath("/home/coder/Algorithms/tree_algorithms"))
from linked_binary_tree import LinkedBinaryTree

class TreeMap(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self._node._element._key
        def value(self):
            return self._node._element._value

    def _subtree_search(self, p, k):
        """ Searches subtree rooted at p for k. if k is not found, at a leaf node, return the leaf"""
        if p.key() == k:
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)
        return p

    def _subtree_first_position(self, p):
        """ Return the first inorder node of the subtree rooted at p """
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk
    
    def _subtree_last_position(self, p):
        """ Return the last inorder node of the subtree rooted at p """
        walk = p 
        while self.right(walk) is  not None:
            walk = self._right(walk)
        return walk
    
    def first(self):
        """ Return the first inorder node of the whole tree """
        return self._subtree_first_position(self.root()) if len(self) > 0 else None
    
    def last(self):
        """ Return the last inorder node of the whole tree """
        return self._subtree_last_position(self.root()) if len(self) > 0 else None
        
    def before(self, p):
        """ Return the inorder predecessor of the node p """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self._parent(walk)
            return above
        
    def after(self, p):
        """ Return the inorder successor of the node p """
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p 
            above = self.parent(walk)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above
        
    def find_position(self, k):
        """ utilize _subtree_search to find the node with key k """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p) # rebalancing hook
            return p
    
    def find_min(self):
        """ Sorted Map Abstraction for tree.first() """
        if self.is_empty():
            return  Npne
        else:
            p = self.first()
            return (p.key(), p.value())
    
    def find_ge(self, k):
        """ Inexact Search for a node with a key that is greater to or equal to k """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key(), p.value())
    
    def find_range(self, start = None, stop = None):
        """ Returns a Range-like yields of nodes satisfying start <= node.key() < stop """
        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield(p.key(), p.value())
                p = self.after(p)
                
    def __getitem__(self, k):
        """ allows key indexing of sorted_map abstraction """
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if p.key() != k:
                raise KeyError('Key Error: ' + repr(k))
            return p.value()
    
    def __setitem__(self, k, v):
        """ Allows changing of value, indexed by the key """
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k :
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)
    
    def items(self):
        """ the sorted map abstraction that returns a tuple of key-value pair """
        p = self.first()
        while p is not None:
            yield  (p.key(), p.value())
            p = self.after(p)

    def __iter__(self):
        """ Iterates in inorder """
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)
    
    def delete(self, p):
        """ Delete a node referenced by position p """
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)
    
    def __delitem__(self, k):
        """ allows del abstraction of the sorted_map structure """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                self.delete(p)
                return
            self._rebalance_acceses(p)
        raise KeyError('Key Error: ' + repr(k))
    
    def _rebalance_insert(self, p): pass
    def _rebalance_delete(self, p): pass
    def _rebalance_access(self, p): pass

    def _relink(self, parent, child, make_left_child):
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):
        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == z._left)
        
        if x == y._left:
            self._relink(y, x._right, True)
            self._relink(x, y, False)
        else:
            self._relink(y, x._left, False)
            self._relink(x, y, True) 
        
    def _restructure(self, x):
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x
        
if __name__ == "__main__":
    rand = random.choices(range(20), k=10)
    d = TreeMap()
    for n in rand:
        d[n] = n*n
    for key, value in d.items():
        print(key, value)
    print(f"min: {d.find_min()}")
    print(f"greater than or equal to 10: {d.find_ge(10)}")
    for key, value in d.find_range(1, 10):
        print(key, value)