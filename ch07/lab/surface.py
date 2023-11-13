from rectangle import Rectangle
class Surface:
    def __init__(self, image, x, y, h, w):
        self.rect = Rectangle(x, y, h, w)
        self.image = str(self.rect)

    def getRect(self):
        return self.rect
