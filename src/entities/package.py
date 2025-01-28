class Package:
    def __init__(self,name,price,coverage_duration, discount = 0.1):
        self.name = name
        self.price = price
        self.coverage_duration = coverage_duration
        self._discount = discount

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if 0 <= discount <= 1:
            self._discount = discount
        else:
            print('Discount must be between 0 and 1')

    @property
    def discounted_price(self):
        return self.price - (self.price * self._discount)