class Rectangle:
    def init (self, x, y, height, width):
        self.x = abs(x)
        self.y = abs(y)
        self.height = abs(height)
        self.width = abs(width)

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def str(self):
        return f"Rectangle: (x: {self.x}, y: {self.y}, width: {self.width}, height: {self.height})"
