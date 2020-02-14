class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __str__(self):
         return f'(x={self.x}, y={self.y})'

v1 = Vector(4,8)
v2 = Vector(3,2)
v3 = Vector(2,6)

vResult = v1 + v2 + v3
print(vResult)