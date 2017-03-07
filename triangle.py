import math

class Point:
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord
    def display(self):
        print "(" + str(self.x) + ", " + str(self.y) + ")"
    def length(self, point):
        return math.sqrt(((point.y-self.y) ** 2) + ((point.x-self.x) ** 2))

class Triangle:
    def __init__(self, p01, p02, p03):
        self.p1 = p01
        self.p2 = p02
        self.p3 = p03
    def display(self):
        self.p1.display()
        self.p2.display()
        self.p3.display()
    def perimeter(self):
        return self.p1.length(self.p2) + self.p2.length(self.p3) + self.p3.length(self.p1)

p1 = Point(1,2)
p2 = Point(3,4)
p3 = Point(5,6)
t1 = Triangle(p1,p2,p3)
t1.display()
print t1.perimeter()
