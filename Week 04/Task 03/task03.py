import math

shape_data = ["rectangle", 5, 4]

match shape_data:
    case ["circle", radius]:
        area = math.pi * (radius**2)
        print("Circle Area: ", area)

    case ["square", side]:
        area = side**2
        print("Square Area: ", area)

    case ["rectangle", length, width]:
        area = length * width
        print("Rectangle Area: ", area)

    case _:
        print("Unknown shape or invalid dimensions")