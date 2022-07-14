class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def get_area(self):
        print(self.length * self.breadth)
    def get_perimeter(self):
        print(2*(self.length + self.breadth))
