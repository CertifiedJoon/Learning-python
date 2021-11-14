from tree_map import TreeMap
import random
class AvlTreeMap(TreeMap):
    class _Node(TreeMap._Node):
        __slots__ = '_heights'
        def __init__ (self, element, parent = None, left = None, right = None):
            super().__init__(element, parent, left, right)
            self._height = 0
        
        def left_height(self, p):
            return self._left._height if self._left is not None else 0
        
        def right_height(self, p):
            return self._right._height if self._right is not None else 0
    
    def _recompute_height(self, p):
        """ Recomputes height of a node referenced by Position p """
        p._node._height = 1 + max(p._node.left._height(), p._node.right_height())
    
    def _isbalanced(self, p):
        """ Checks whether if subtree rooted at p is balanced """
        return abs(p._node.right_height() - p._node.left_height()) <= 1
    
    def _tall_child(self, p, favoreft = False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)
    
    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not not self._isbalanced(p):
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old._height:
                p = None
            else:
                p = self.parent(p)
    
    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rabalance_delete(self, p):
        self._rebalance(p)
    
    def _rebalance_access(self, p):
        self._rebalance(p)

if __name__ == "__main__":
    rand = random.choices(range(20), k=10)
    d = TreeMap()
    for n in rand:
        d[n] = n*n
    for key, value in d.items():
        print(key, value)
    print(f"min: {d.find_min()}")
    print(f"greater than or equal to 10: {d.find_ge(10)}")
    listed = d.list_by_depth()
    for depth in listed:
        for item in depth:
            print(item._key, item._value, end="     ")
        print("")
    for key, value in d.find_range(1, 10):
        print(key, value)