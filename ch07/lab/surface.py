from rectangle import Rectangle

class Surface:
    def __init__(self, filename, x, y, h, w):
        self.image_filename = filename
        self.rect = Rectangle(x, y, h, w)

    def calculate_area(self):
        return self.rect.calculate_area()

    def calculate_perimeter(self):
        return self.rect.calculate_perimeter()

    def getRect(self):
        return self.rect

    def __str__(self):
        return f"Surface(image={self.image_filename}, rect={str(self.rect)})"

my_surface = Surface(filename="example.jpg", x=0, y=0, h=5, w=10)

print(f"Rectangle: {my_surface.getRect()}")
print(f"Image: {my_surface.image_filename}")

print(str(my_surface))
