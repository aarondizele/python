import math

class Geometry:

    def __init__(self, shape):
        self.shape = shape

    def rectangle_area(self):
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            area = length * width
            return "The area of the rectangle is {}".format(area)

    def circle_area(self):
        radius = float(input("Enter the radius: "))
        area = math.pi * (math.pow(radius,2))
        return "The area of the circle is {:.2f}".format(area)

    def get_area(self, shape):
        shape = self.shape
        shape = shape.lower()
        if shape == "rectangle":
            return self.rectangle_area()
        elif shape == "circle":
            return self.circle_area()
        else:
            return "Please enter rectangle or circle"

    def get_result(self):
        return self.get_area(self.shape)

def main():

    shape = input("Get area for what shape : ")
    geo = Geometry(shape)
    print(geo.get_result())

if __name__ == '__main__':
    main()