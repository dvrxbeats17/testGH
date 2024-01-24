class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, p):
        result = (self.x + p.x, self.y + p.y)
        return self.x + p.x, self.y + p.y

    def __eq__(self, p):
        return self.x == p.x and self.y == p.x

    def __sub__(self, p):
        return self.x - p.x, self.y - p.y

    @property
    def length(self):
        return

a = Point(5, 10)
b = Point(1, 3)
print(a + b)
print(a != b)
print(a - b)