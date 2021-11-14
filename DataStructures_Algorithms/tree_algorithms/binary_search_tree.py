from linked_binary_tree import LinkedBinaryTree

class BinarySearchTree(LinkedBinaryTree):
    def __init__(self, sorted_array = None):
        self._root = None
        self._size = 0
        if sorted_array is not None:
            self.create_minimal_bst(sorted_array)
    
    def create_minimal_bst(self, array):
        """Wrapper for self._rec_create_minimal_bast(array, start, end) method"""
        self._rec_create_minimal_bst(array, 0, len(array)-1)
        
    def _rec_create_minimal_bst(self, array, start, end):
        """Create a binary search tree with minimal height from a sorted array"""
        if end < start:
            return
        mid = start + (end - start) // 2
        self.insert(array[mid])
        self._rec_create_minimal_bst(array, start, mid - 1)
        self._rec_create_minimal_bst(array, mid + 1, end)
        
    def insert(self, element):
        """inserts an element to a tree"""
        if self.is_empty():
            self._add_root(element)
            return
        curr = self.root()
        parent = None
        while curr:
            parent = curr
            if element < curr.element():
                curr = self.left(curr)
            else:
                curr = self.right(curr)
        self._add_left(parent, element) if element < parent.element() else self._add_right(parent, element)
        
    def get_all_sequences(self):
        if self.is_empty():
            return []
        ret_backtracked = []
        def backtracking(choices, sofar):
            if not choices:
                ret_backtracked.append(sofar)
                return
            for i in range(len(choices)):
                new_choices = choices[:i] + choices[i+1:]
                if self.left(choices[i]):
                    new_choices.append(self.left(choices[i]))
                if self.right(choices[i]):
                    new_choices.append(self.right(choices[i]))
                backtracking(new_choices, sofar + [choices[i].element()])
        backtracking([self.root()], [])
        return ret_backtracked            

if __name__ == "__main__":
    bst = BinarySearchTree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
    bst.preorder_indented()
    print(bst.count_path_sum(6))
    for i in range(1, 20):
        print(f"{i} has {bst.count_path_sum(i)} paths")