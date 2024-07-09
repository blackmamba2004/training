class Payments:
    payments_count = 0

    def __init__(self, money):
        self.money = money
        self.__class__.payments_count += 1

    @classmethod
    def get_payments(cls):
        return cls.payments_count

    def __setattr__(self, key, value):
        if key == 'payments_count':
            raise AttributeError('Доступ закрыт')
        return super().__setattr__(key, value)


p1 = Payments(100)
p2 = Payments(200)
p3 = Payments(300)
Payments.payments_count += 1
print(p1.payments_count)
# print(Payments.__dict__.keys())