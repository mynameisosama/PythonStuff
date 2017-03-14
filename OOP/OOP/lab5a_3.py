import math

class Point(object):
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
    def display(self):
        print (self.x,self.y)
    def length(self, point):
        return math.sqrt(((point.y-self.y) ** 2) + ((point.x-self.x) ** 2))
class Rectangle(object):
    def __init__(self, point1, point2):
        self.length = abs(point1.x - point2.x)
        self.height = abs(point1.y - point2.y)
    def area(self):
        return self.length*self.height
    def perimeter(self):
        return 2*(self.length+self.height)
    def isGreater(self, rectangle):
        if self.area() > rectangle.area():
            return True
        else:
            return False
    def display(self):
        print("Area: " + str(self.area()))
        print("Perimeter: " + str(self.perimeter()))

r1 = Rectangle(Point(1,2),Point(4,5))
r1.display()
r2 = Rectangle(Point(2,3),Point(5,6))
r2.display()
print(r1.isGreater(r2))
