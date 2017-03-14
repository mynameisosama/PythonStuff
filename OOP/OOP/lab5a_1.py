import math

class Point(object):
    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor
    def length(self, p):
        return math.sqrt((p.y-self.y)**2 + (p.x-self.x)**2)
    def display(self):
        print(self.x,self.y)
class Circle(object):
    def __init__(self, rad, point):
        self.r = rad
        self.p = point
    def display(self):
        print("radius: " + str(self.r))
        print("center: " + str(self.p.x) + ", " + str(self.p.y))
class Cone(object):
    def __init__(self, circle, point):
        self.r = circle.r
        self.h = abs(point.y - circle.p.y)
        p = Point(circle.p.x + circle.r, circle.p.y)
        self.s = p.length(point)
    def display(self):
        print("radius: " + str(self.r))
        print("height: " + str(self.h))
        print("slope: " + str(self.s))
    def volume(self):
        return (3.14 * (self.r**2) * self.h)/3


cone = Cone(Circle(5,Point(2,3)), Point(5,6))
cone.display()
print("volume: " + str(cone.volume()))
        
