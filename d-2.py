import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return round(self.height * self.width, 2)

    def diagonal(self):
        return round(math.sqrt(self.height**2 + self.width**2), 2)


# 高さ5、幅6の長方形
rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

# 高さ3、幅3の長方形
rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
