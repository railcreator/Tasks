import pytest
from src.module.engine2d import Engine2D, Circle, Rectangle, Triangle

@pytest.fixture
def engine():
    return Engine2D()

@pytest.fixture
def circle():
    return Circle(0, 0, 1)

@pytest.fixture
def rectangle():
    return Rectangle(0, 0, 2, 3)

@pytest.fixture
def triangle():
    return Triangle((0, 0), (1, 1), (2, 2))

@pytest.mark.parametrize("color", ["red", "green", "blue"])
def test_set_color(engine, color):
    engine.set_color(color)
    assert engine.color == color

def test_add_figure(engine, circle):
    engine.add_figure(circle)
    assert len(engine.figures) == 1
    assert engine.figures[0] == circle

def test_add_figure_with_color(engine, circle):
    engine.set_color("red")
    engine.add_figure(circle)
    assert len(engine.figures) == 1
    assert engine.figures[0] == circle
    assert engine.colors[0] == "red"

def test_add_figure_without_color(engine, circle):
    engine.add_figure(circle)
    assert len(engine.figures) == 1
    assert engine.figures[0] == circle
    assert engine.colors[0] == "black"

def test_draw_no_figures(engine):
    engine.draw()
    assert len(engine.figures) == 0

def test_draw_with_figures(engine, circle, rectangle, triangle):
    engine.add_figure(circle)
    engine.add_figure(rectangle)
    engine.add_figure(triangle)
    engine.draw()
    assert len(engine.figures) == 0
    assert len(engine.colors) == 0

@pytest.mark.parametrize("color", ["red", "green", "blue"])
def test_draw_with_color(engine, circle, rectangle, triangle, color):
    engine.add_figure(circle)
    engine.add_figure(rectangle)
    engine.add_figure(triangle)
    engine.set_color(color)
    engine.draw()
    assert len(engine.figures) == 0
    for c in engine.colors:
        assert c == color

def test_set_color_multiple_times(engine):
    engine.set_color("red")
    engine.set_color("green")
    engine.set_color("blue")
    assert engine.color == "blue"