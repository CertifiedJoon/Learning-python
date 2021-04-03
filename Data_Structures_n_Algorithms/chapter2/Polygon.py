from abc import ABCMeta, abstractmethod
from math import sqrt

class Polygon(metaclass=ABCMeta):
    def __init__(self, vertices):
        self._vertices = vertices
        
    @abstractmethod
    def area(self):
        """Return the area enclosed by polygon"""
        
    @abstractmethod
    def perimeter(self):
        """Return the length of contours of the polygon"""
        
class Triangle(Polygon):
    def __init__(self, vertices):
        """initialize vertices as three pairs of coordinates"""
        super().__init__(vertices)
        self._a = sqrt(pow((self._vertices[0][0] - self._vertices[1][0]), 2) + pow((self._vertices[0][1] - self._vertices[1][1]), 2))
        self._b = sqrt(pow((self._vertices[1][0] - self._vertices[2][0]), 2) + pow((self._vertices[1][1] - self._vertices[2][1]), 2))
        self._c = sqrt(pow((self._vertices[2][0] - self._vertices[0][0]), 2) + pow((self._vertices[2][1] - self._vertices[0][1]), 2)) 
        
    def perimeter(self):
        """Returns a + b + c"""
        return self._a + self._b + self._c
    
    def area(self):
        s = self.perimeter() / 2
        return sqrt(s*(s-self._a)*(s-self._b)*(s-self._c))
    
class Quadrilateral(Polygon):
    def __init__(self, vertices):
        super().__init__(vertices)
        self._triangle1 = Triangle(vertices[:3])
        self._triangle2 = Triangle((vertices[0], vertices[2], vertices[3]))
        
    def perimeter(self):
        return self._triangle1.perimeter() + self._triangle2.perimeter() - self._triangle1._b * 2
    
    def area(self):
        return self._triangle1.area() + self._triangle2.area()
    
class Pentagon(Polygon):
    def __init__(self, vertices):
        """User must enter the vertices in a clockwise order"""
        super().__init__(vertices)
        self._quadrilateral1 = Quadrilateral(vertices[:4])
        self._triangle1 = Triangle ((vertices[0],vertices[3],vertices[4]))
        
    def perimeter(self):
        return self._quadrilateral1.perimeter() + self._triangle1.perimeter() - self._triangle1._a * 2
    
    def area(self):
        return self._quadrilateral1.area() + self._triangle1.area()


t = Triangle(((0,0), (2,0), (0,2)))
q = Quadrilateral(((0,0), (2,0), (0,2), (2,2)))
p = Pentagon(((2,2), (4,1), (3,0), (1,0), (0,1)))

print("Triangle is {:.3} large and {:.3} in perimeter".format(t.area(), t.perimeter()))
print("Quadrilateral is {:.3} large and {:.3} in perimeter".format(q.area(), q.perimeter()))
print("Pentagon is {:.3} large and {:.3} in perimeter".format(p.area(), p.perimeter()))