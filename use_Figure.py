from Figure import GeomFigure, Rectangle, Square, Circle

g_fig = GeomFigure()
rect_1 = Rectangle(10, 2)
rect_2 = Rectangle(5, 3)
square_1 = Square(4)
circle_1 = Circle(3)

figures = [g_fig, rect_1, rect_2, square_1, circle_1]
for fig in figures:
    print(f"{fig}. Area = {fig.get_area()}")
