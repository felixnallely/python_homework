#Task 5:
import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#equality 
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y 
#String Representation
    def __str__(self):
        return f"Point(x= {self.x}, y= {self.y})"
#Euclidian distance
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"
    def __add__(self, other):
        if not isinstance(other, Vector):
            return TypeError
        return Vector(self.x + other.x, self.y + other.y)

if __name__ == "__main__":
    p1 = Point(4, 5)
    p2 = Point(2, 3)
    p3 = Point(0, 0)

    print("Point equality: ", p1 == p2)
    print("Point string: ", p1)
    print("Distance p1 -> p3: ", p1.distance(p3))

    v1 = Vector(2, 3)
    v2 = Vector(3, 5)

    print("Vector string:", v1)
    print("Vector add: ", v1 + v2)
    print("Vector distance:", v1.distance(v2))