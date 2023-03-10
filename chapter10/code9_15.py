class Circle:
    PI = 3.1415
    def __init__(self, name, radius):
        self.__name = name
        self.__radius = radius
        
    def area(self):
        return Circle.PI * self.__radius ** 2
    
c1 = Circle("C1", 4)
print("c1의 면적:", c1.area())
c2 = Circle("C2", 6)
print("c2의 면적:", c2.area())
c3 = Circle("C3", 5)
print("c3의 면적:", c3.area())