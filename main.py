"""Circle"""


class Circle:
    """Square circle"""
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """area circle"""
        return self.pi * self.radius ** 2


circle = Circle(10)
area = circle.area()
print(area)
