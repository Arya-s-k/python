class Circle:  
    def area(self, radius):
        area1 = 3.14 * (radius ** 2)
        return area1

    def perimeter(self, radius):
        perimeter = 2 * 3.14 * radius
        return perimeter

    def getradius(self):
        radius = float(input("What is the radius of the circle (cm): "))
        return radius

circle1 = Circle()

radius = circle1.getradius()
print("Area:", circle1.area(radius),"cm")
print("Perimeter:", circle1.perimeter(radius),"cm")
