class rectangle:
    def __init__(self, length, width, cost):
            self.length = length
            self.width = width
            self.cost = cost

    def get_area(self):
        return self.length * self.width

    def get_price(self):
        area = self.get_area()
        return area *self.cost


