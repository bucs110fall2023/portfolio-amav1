from rectangle import Rectangle

class Surface:
    def init(self, filename, x, y, h, w):
     self.image = filename
     self.rect = Rectangle(x, y, h, w)

    def calculate_area(self):
        return self.rect.calculate_area()

    def calculate_perimeter(self):
        return self.rect.calculate_perimeter()

    def getRect(self):
       return self.rect

    def str(self):
        return f"Surface(image={self.image}, rect={str(self.rect)})"

my_surface = Surface(filename="example.jpg", x=0, y=0, h=5, w=10)

print(f"Rectangle: {my_surface.getRect()}")
print(f"Image: {my_surface.image}")

print(str(my_surface))