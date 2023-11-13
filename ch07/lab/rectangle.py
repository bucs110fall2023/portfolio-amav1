class Rectangle:
    def __init__ (self, x, y, h, w):
        self.x = x
        self.y = y
        self.height = h 
        self.width = w

    def __str__(self):
        return f"Rectangle(x={self.x}, y={self.y}, height={self.height}, width={self.width})"
