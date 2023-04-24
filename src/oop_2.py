from src.module.engine2d import Engine2D, Circle, Rectangle, Triangle

if __name__ == "__main__":
    engine = Engine2D()
    circle = Circle(0, 0, 1)
    rectangle = Rectangle(0, 0, 2, 3)
    triangle = Triangle((0, 0), (1, 1), (2, 2))

    engine.add_figure(circle)
    engine.add_figure(rectangle)
    engine.add_figure(triangle)
    engine.draw()

    engine.set_color("red")
    circle2 = Circle(1, 1, 2)
    rectangle2 = Rectangle(2, 2, 3, 4)
    triangle2 = Triangle((3, 3), (4, 4), (5, 5))

    engine.add_figure(circle2)
    engine.add_figure(rectangle2)
    engine.add_figure(triangle2)

    for figure in engine.figures:
        figure.set_color(engine.color)
    engine.draw()

    circle3 = Circle(1, 1, 2)
    rectangle3 = Rectangle(2, 2, 3, 4)
    triangle3 = Triangle((3, 3), (4, 4), (5, 5))

    engine.add_figure(circle3)
    engine.add_figure(rectangle3)
    engine.add_figure(triangle3)

    for figure in engine.figures:
        figure.set_color(engine.color)
    engine.draw()