from Figure import Rectangle, Square, Circle


rect_1 = Rectangle(10, 2)
rect_2 = Rectangle(5, 3)
square_1 = Square(4)
circle_1 = Circle(3)

figures = [rect_1, rect_2, square_1, circle_1]
for fig in figures:
    print(f"Area of {fig.__class__.__name__} = {fig.get_area()}")
