class ShapeCalculator:
    def calculate_area(self, shape_type, **kwargs):
        if shape_type == "circle":
            return self.calculate_circle_area(kwargs["radius"])
        elif shape_type == "rectangle":
            return self.calculate_rectangle_area(kwargs["length"], kwargs["width"])
        elif shape_type == "triangle":
            return self.calculate_triangle_area(kwargs["base"], kwargs["height"])
        else:
            raise ValueError("Invalid shape type.")

    def calculate_circle_area(self, radius):
        return 3.14 * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width

    def calculate_triangle_area(self, base, height):
        return 0.5 * base * height


calculator = ShapeCalculator()

shape_type = input("Enter the type of shape (circle, rectangle, triangle): ")

if shape_type == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = calculator.calculate_area(shape_type, radius=radius)
elif shape_type == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = calculator.calculate_area(shape_type, length=length, width=width)
elif shape_type == "triangle":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = calculator.calculate_area(shape_type, base=base, height=height)
else:
    print("Invalid shape type.")
    exit()

print("Area:", area)
