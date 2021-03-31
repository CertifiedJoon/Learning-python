class Flower:
    def __init__(self, name, number, price):
        """Flower class that contains name(str), number of petals(int)
        and price(float)"""
        self.name_ = name
        self.petals_ = number
        self.price_ = price

    def get_name(self):
        return self.name_

    def get_petals(self):
        return self.petals_

    def get_price(self):
        return self.price_

    def set_name(self, s):
        self.name_ = s

    def set_petals(self, n):
        self.petals_ = n

    def set_price(self, p):
        self.price_ = p


flora = Flower("Lily", 4, 15.0)
print(flora.get_name(), flora.get_petals(), flora.get_price())

flora.set_name("Lilac")
flora.set_petals(5)
flora.set_price(18.0)
print(flora.get_name(), flora.get_petals(), flora.get_price())
