class Vector:
    """represent a vector in a multidimensional space"""
    
    def __init__(self, d):
        if (isinstance(d, int)):
            self._coords = [0] * d
        elif (isinstance(d, collection.Iterable)):
            self._coords = Vector(len(d))
            for j in range(len(d)):
                self._coords[j] = d[j]
                
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self, j):
        retun self._coords[j]
    
    def __setitem__(self, j, val):
        self._coords[j] = val
    
    def __add__(self, other):
        """return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('vectors must be in the same dimension')
        result = Vector(len(self))
        
        for j in range (len(self)):
            result[j] = self[j] + other[j]
        
        return result
    
    def __radd__(self, other):
        """return sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('vectors must be in the same dimension')
        result = Vector(len(self))
        
        for j in range (len(self)):
            result[j] = self[j] + other[j]
        
        return result
    
    def __eq__(self, other):
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other
    
    def __sub__(self, other):
        """return difference between two vectors""""
        if len(self) != len(other):
            raise ValueError('vectors must be in same dimension')
        result = Vector(len(self))
        
        for j in range (len(self)):
            result[j] = self[j] - other[j]
            
        return result
    
    def __neg__(self):
        result = Vector(len(self))
        
        for j in range (len(self)):
            result[j] = -self[j]
            
    def __str__(self):
        return '<' + str(self._coords)[1:-1] +'>'
    
    def __mul__(self, k):
        if len(self) != len(other):
            raise ValueError('vectors must be in same dimension')
            
        return sum(self[k] * other[k] for k in range(len(self)))
            
    def __rmul__ (self, k):
        result = Vector (len(self))
        
        for j in range (len(self)):
            result[i] *= k