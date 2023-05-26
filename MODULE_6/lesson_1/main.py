class Tortburchak:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # method
    def peremetr(self):
        return self.a * 2 + self.b * 2

    # method
    def yuza(self):
        return self.a * self.b


obj = Tortburchak(10, 10)

print(obj.yuza())
