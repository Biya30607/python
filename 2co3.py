import math

class rectangle:
    @staticmethod
    def area(length, width):
        return length * width
    
    @staticmethod
    def perimeter(length, width):
        return 2 * (length + width)

class circle:
    @staticmethod
    def area(radius):
        return math.pi * radius * radius

    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

class cuboid:
    @staticmethod
    def area(l, w, h):
        return 2 * (l*w + w*h + h*l)

    @staticmethod
    def perimeter(l, w, h):
        return 4 * (l + w + h)

class sphere:
    @staticmethod
    def area(radius):
        return 4 * math.pi * radius * radius

    @staticmethod
    def perimeter(radius):
        return 2 * math.pi * radius

print("=== PROGRAM 1: NORMAL IMPORT ===")
rect = rectangle
circ = circle
cub = cuboid
sph = sphere

print("Rectangle area:", rect.area(10, 20))
print("Rectangle perimeter:", rect.perimeter(10, 20))
print("Circle area:", circ.area(7))
print("Circle perimeter:", circ.perimeter(7))
print("Cuboid area:", cub.area(2, 3, 4))
print("Cuboid perimeter:", cub.perimeter(2, 3, 4))
print("Sphere area:", sph.area(5))
print("Sphere perimeter:", sph.perimeter(5))

print("\n=== PROGRAM 2: SELECTIVE IMPORT ===")
r_area = rectangle.area
r_peri = rectangle.perimeter
c_area = circle.area
c_peri = circle.perimeter
cu_area = cuboid.area
s_peri = sphere.perimeter

print("Rectangle area:", r_area(4, 5))
print("Rectangle perimeter:", r_peri(4, 5))
print("Circle area:", c_area(6))
print("Circle perimeter:", c_peri(6))
print("Cuboid area:", cu_area(1, 2, 3))
print("Sphere perimeter:", s_peri(7))

print("\n=== PROGRAM 3: IMPORT * ===")
area = rectangle.area
perimeter = rectangle.perimeter
print("Rectangle area:", area(3, 7))
area = circle.area
print("Circle area:", area(5))
area = cuboid.area
print("Cuboid area:", area(2, 2, 2))
perimeter = sphere.perimeter
print("Sphere perimeter:", perimeter(4))
