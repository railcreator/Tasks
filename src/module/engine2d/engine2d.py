class Engine2D:
    def __init__(self):
        self.figures = []
        self.color = "black"
        self.colors = []

    def add_figure(self, figure):
        figure.set_color(self.color)
        self.figures.append(figure)
        self.colors.append(self.color)

    def set_color(self, color):
        self.color = color
        for i in range(len(self.figures)):
            self.colors[i] = color
            self.figures[i].set_color(color)

    def draw(self):
        for figure in self.figures:
            figure.draw()
        self.figures = []
        self.colors = []


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = "black"

    def set_color(self, color):
        self.color = color

    def draw(self):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} and color {self.color}")


class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "black"

    def set_color(self, color):
        self.color = color

    def draw(self):
        print(f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height} and color {self.color}")


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.color = "black"

    def set_color(self, color):
        self.color = color

    def draw(self):
        print(f"Drawing Triangle: ({self.point1}, {self.point2}, {self.point3}) with color {self.color}")

